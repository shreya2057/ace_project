import datetime
import os

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from . import db
from .models import Doctor, Patient, User
from werkzeug.utils import secure_filename

from . import app
from .models import Scan

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('home.html',user=current_user)

@views.route('/docprofile')
def profile():
	return render_template('docprofile.html',user=current_user)

@views.route('/patientProfile')
def patient():
	patient = Patient.query.filter_by(id = current_user.id).first()
	print(patient.scans)
	scan = Scan.query.filter_by(user_id = current_user.id).first()
	return render_template('patientprofile.html',user=current_user, patient=patient, scans=scan)


@views.route('/doccard')
def card():
	return render_template('doccard.html',user=current_user)

app.config['SCAN_UPLOAD'] = 'static/images/uploads/scans'

@views.route('/upload-scan',methods=['POST'])
@login_required
def upload_scan():
	if request.method == 'POST':
		if request.files:
			image = request.files['scan']
			# filename=f'scan-{current_user.name}-{datetime.datetime.now()}{os.path.splitext(image.filename)[1]}'
			# image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD'],secure_filename(filename)))
			uri = upload_image(image, 'scan')
			new_scan = Scan(uri=uri,user_id=current_user.id)
			flash('Scan successfully uploaded.',category='success')
	return redirect(url_for('views.home'))

def upload_image(image,type):
	filename=f'{type}-{current_user.name}-{datetime.datetime.now()}{os.path.splitext(image.filename)[1]}'
	image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD'],secure_filename(filename)))
	return f'{app.config["SCAN_UPLOAD"]}/{filename}'


