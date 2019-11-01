"""
Example of SQL Alchemy ORM set up for a US State table.

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/geospatial_usa_states'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class States(db.Model):
    __tablename__ = 'us_state'
    gid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String)
    division = db.Column(db.String)
    statefp = db.Column(db.String)
    statens = db.Column(db.String)
    geoid = db.Column(db.String)
    stusps = db.Column(db.String)
    name = db.Column(db.String)
    lsad = db.Column(db.String)
    mtfcc = db.Column(db.String)
    funcstat = db.Column(db.String)
    aland = db.Column(db.Float)
    awater = db.Column(db.Float)
    intptlat = db.Column(db.String)
    intptlon = db.Column(db.String)
    geom = db.Column(Geometry('POLYGON'))


state_records = States.query.all()
