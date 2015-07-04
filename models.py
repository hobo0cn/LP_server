# from db import Column, DateTime, String, Integer, ForeignKey, func
# from sqlalchemy.orm import relationship, backref
from database import db
from datetime import datetime

class Ship(db.Model):
    __tablename__ = 'ship'
    id = db.Column( db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    capacity = db.Column(db.Integer)

    histories =db.relationship("ShipHistory", backref="ship", order_by="ShipHistory.id")

    def __init__(self, name=None, capacity=0):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return '<Ship %s,%r>' % (self.name, self.capacity)


class ShipHistory(db.Model):
    __tablename__ = 'ship_history'
    id = db.Column(db.Integer, primary_key=True)
    arrive_date = db.Column(db.DateTime)
    oil_name = db.Column(db.String(50))
    value = db.Column(db.Integer)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'))

    def __init__(self, arrive_date, oil_name, value=0):
        self.arrive_date = arrive_date
        self.oil_name = oil_name
        self.value = value
        self.arrive_date = datetime.utcnow()


    def __repr__(self):
        return '<Ship_history %s, %s, %s>' % (self.arrive_date, self.oil_name, self.value)



    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    # ship = db.relationship(
    #     Ship,
    #     backref=backref('ship_histories',
    #                      uselist=True,
    #                      cascade='delete,all'))

