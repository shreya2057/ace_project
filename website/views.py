import datetime
import os
import pickle

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import app, db
from .models import Doctor, Patient, Scan

views = Blueprint('views', __name__)
tb_model = pickle.load(open('TB.pkl','rb'))
pneumonia_model = pickle.load(open('PN.pkl','rb'))
tumor_model = pickle.load(open('tumor.pkl','rb'))
@views.route('/')
def home():
	return render_template('home.html',user=current_user)

@views.route('/docprofile')
def profile():
	return render_template('docprofile.html',user=current_user)

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
			type = request.form.get('type')
			uri = upload_image(image, 'scan')
			new_scan = Scan(uri=uri,user_id=current_user.id, type = type)
			db.session.commit()
			pred = prediction(type, image)
			flash('Scan successfully uploaded.',category='success')
	return redirect(url_for('views.home'),data=pred)

def prediction(type, image):
	if type=='Tuberculosis':
		flash('TB')
		pred = tb_model.predict(image)
	elif type=='Brain Tumor':
		flash('tumor')
		pred = tumor_model.predit(image)
	elif type=='Penumonia':
		flash('pneumonia')
		pred = pneumonia_model(image)
	return pred

def upload_image(image,type):
	filename=f'{type}-{current_user.name}-{datetime.datetime.now()}{os.path.splitext(image.filename)[1]}'
	image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD'],secure_filename(filename)))
	return f'{app.config["SCAN_UPLOAD"]}/{filename}'