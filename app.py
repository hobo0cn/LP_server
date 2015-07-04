from flask import Flask
import os
from database import db

__curdir__ = os.path.realpath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    # app.config['DEBUG'] = True
    #
    # app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///" +__curdir__ + "/LP.db"

    app.config.from_pyfile('app.cfg')

    db.init_app(app)

    from ship import ship_bp
    app.register_blueprint(ship_bp)
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app()
    #Because this is just a demostration we set up the database like this.
    if not os.path.isfile(__curdir__ + "/LP.db"):
      setup_database(app)

    app.run()



