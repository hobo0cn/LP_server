from flask import Blueprint
from flask_restful import Api, Resource
from flask_restful import reqparse, abort
from models import Ship
from database import db

ship_bp = Blueprint('ship', __name__)
api = Api(ship_bp)


SHIPS = {
    'ship1': {'name': '501', 'capacity': 1000},
    'ship2': {'name': '502', 'capacity': 2000},
    'ship3': {'name': '503', 'capacity': 3000},
}


def abort_if_ship_doesnt_exist(ship_id):
    if ship_id not in SHIPS:
        abort(404, message="Ship {} doesn't exist".format(ship_id))

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('capacity', type=int)

# ShipList
# shows a list of all ships, and lets you POST to add new ship record
class ShipList(Resource):

    ships = {}
    # @property
    def get(self):
        self.ships = {}
        ship_query = Ship.query.all()

        for ship in ship_query:
            self.ships[ship.id] = {'name': ship.name, 'capacity': ship.capacity}

        return self.ships


    def post(self):
        args = parser.parse_args()
        n = args['name']
        c = args['capacity']
        newShip = Ship(n, c)
        db.session.add(newShip)

      	db.session.commit()
        self.ships[newShip.id] = {'name': newShip.name, 'capacity': newShip.capacity}
        return self.ships, 201


#shows a single todo item and lets you delete a todo item
class Ship_view(Resource):
    def get(self, ship_id):
        abort_if_ship_doesnt_exist(ship_id)
        return SHIPS[ship_id]

    def delete(self, ship_id):
        abort_if_ship_doesnt_exist(ship_id)
        del SHIPS[ship_id]
        return '', 204

    def put(self, ship_id):
        args = parser.parse_args()
        task = {'name': args['name'], 'value': args['value']}
        SHIPS[ship_id] = task
        return task, 201


##
## Actually setup the Api resource routing here
##
api.add_resource(ShipList, '/ships')
api.add_resource(Ship_view, '/ships/<ship_id>')

