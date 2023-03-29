"""
This file contains the models for the sprocketFactory app.
"""
# pylint: disable=too-few-public-methods


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Factory(db.Model):
    """
    This class is a ORM model for the factories table.

    It has a one to one relationship with the production table.
    """
    __tablename__ = 'factories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    chart_data = db.relationship('Production', backref='factories')

class Production(db.Model):
    """
    This class is a ORM model for the production table.
    """
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
    sprocket_production_actual = db.Column(db.Integer)
    sprocket_production_goal = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    factory_id = db.Column(db.Integer, db.ForeignKey('factories.id'))

class Sprocket(db.Model):
    """
    This class is a ORM model for the sprockets table.
    """
    __tablename__ = 'sprockets'
    id = db.Column(db.Integer, primary_key=True)
    teeth = db.Column(db.Integer)
    pitch_diameter = db.Column(db.Float)
    outside_diameter = db.Column(db.Float)
    pitch = db.Column(db.Float)
