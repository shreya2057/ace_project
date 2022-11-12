import datetime
import os

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import app, db
from .models import Doctor, Scan

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('home.html',user=current_user)

@views.route('/docprofile')
@login_required
def docprofile():
	doctor = Doctor.query.filter_by(id=request.args.get('id')).first()
	is_current = False
	if doctor.id == current_user.id:
		is_current = True
	# print(current_user.user.name,current_user.user.email,current_user.dob)
	return render_template('docprofile.html',user=current_user,doctor=doctor, is_current=is_current)

@views.route('/doccard')
def card():
	return render_template('doccard.html',user=current_user)

app.config['SCAN_UPLOAD'] = 'static/images/uploads/scans'
app.config['LICENSE_UPLOAD'] = 'static/images/uploads/license'

@views.route('/upload-scan',methods=['POST'])
@login_required
def upload_scan():
	if request.method == 'POST':
		if request.files:
			image = request.files['scan']
			uri = upload_image(image, 'scan')
			new_scan = Scan(uri=uri,user_id=current_user.id)
			db.session.commit()
			flash('Scan successfully uploaded.',category='success')
	return redirect(url_for('views.home'),user=current_user)

@views.route('/upload-license',methods=['POST'])
@login_required
def upload_license():
	if request.method == 'POST':
		if request.files:
			image = request.files['license']
			uri = upload_image(image, 'license')
			current_user.license = uri
			db.session.commit()
			flash('License successfully uploaded.', category='success')
		else:
			flash('No files found.',category='error')
	return redirect(url_for('views.docprofile'),user=current_user)

def upload_image(image,type):
	filename=f'{type}-{current_user.name}-{datetime.datetime.now()}{os.path.splitext(image.filename)[1]}'
	image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD' if type=='scan' else 'LICENSE_UPLOAD'],secure_filename(filename)))
	return f'{app.config["SCAN_UPLOAD"]}/{filename}'