from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import Doctor, Patient, User

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()
		if user:
			if check_password_hash(user.password, password):
				flash('Logged in successfully',category='success') #message flash
				if(user.role=='Patient'):
					loggedUser = Patient.query.filter_by(user_id=user.id).first()
				else:
					loggedUser = Doctor.query.filter_by(user_id=user.id).first()
				login_user(loggedUser)
				flash('Logged In Successfully.',category='success')
				return redirect(url_for('views.home'))
			else:
				flash('Incorrect password.',category='error')
		else:
			flash('Incorrect email.',category='error')
	return render_template("login.html",user=current_user)

@auth.route('/signup',methods=['GET','POST'])
def signup():
	if(request.method == 'POST'):
		name = request.form.get('name')
		email = request.form.get('email')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		gender = request.form.get('gender')
		phone= request.form.get('phone')
		role = request.form.get('role')
		if role == 'Patient':
			dob = request.form.get('dob')
		else:
			nmc_number = request.form.get('nmcNumber')
			practice_years = request.form.get('practice_years')
			expertise =request.form.get('expertise')
			hospital =request.form.get('hospital')
			qualification =request.form.get('qualification')

		ex_user = User.query.filter_by(email=email).first()
		if ex_user:
			flash('User already exists.',category='error')
		elif len(name)<3:
			flash('Invalid Name.',category='error')
		elif len(email)<5:
			flash('Invalid email.',category='error')
		elif len(gender)<1:
			flash('Invalid gender.',category='error')
		elif len(str(phone))<5:
			flash('Invalid phone.',category='error')
		elif password1 != password2:
			flash('Passwords do not match.',category='error')
		elif len(password1) <8:
			flash('Password length should be greater than 8.',category='error')
		else:
			new_user = User(name=name, email=email, password =generate_password_hash(password1,method='sha256'),gender =gender,phone =phone,role =role)
			db.session.add(new_user)
			db.session.commit()
			if(role == 'Patient'):
				new_patient = Patient(dob = dob, user_id = new_user.id)
				db.session.add(new_patient)
			else:
				new_doctor=Doctor(nmc_number = nmc_number,practice_years=practice_years,expertise=expertise,hospital=hospital,qualification=qualification, user_id = new_user.id)
				db.session.add(new_doctor)
			db.session.commit()
			login_user(new_patient,remember=True)
			flash('Signed Up Successfully.',category='success')

			return redirect(url_for('views.home'))
	return render_template("signup.html",user=current_user)
	
