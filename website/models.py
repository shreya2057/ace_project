from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class Scan(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	scanned_date=db.Column(db.DateTime(timezone=True),default=func.now())
	uri=db.Column(db.String(300))
	user_id = db.Column(db.Integer,db.ForeignKey('patient.id'))
	result = db.Column(db.String(100))

class User(db.Model,UserMixin):
	id=db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150))
	email=db.Column(db.String(150),unique=True)
	password = db.Column(db.String(150))
	gender = db.Column(db.String(10))
	phone = db.Column(db.BigInteger)
	role = db.Column(db.String(20))

class Patient(db.Model,UserMixin):
	id=db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
	# id = db.Column(db.Integer,primary_key=True)
	dob = db.Column(db.String(20))
	scans = db.relationship('Scan')
	user = db.relationship('User')


class Doctor(db.Model, UserMixin):
	# id = db.Column(db.Integer,primary_key=True)
	id=db.Column(db.Integer,db.ForeignKey('user.id'),primary_key=True)
	license = db.Column(db.String(300),nullable=True)
	nmc_number = db.Column(db.BigInteger)
	practice_years = db.Column(db.Integer)
	expertise = db.Column(db.String(200))
	hospital = db.Column(db.String(200))
	qualification = db.Column(db.String(100))
	user = db.relationship('User')
