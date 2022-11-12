import datetime
import os
import pathlib
import pickle as pkl

import numpy as np
import PIL
import tensorflow as tf
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from PIL import Image
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

from . import app, db
from .models import Doctor, Patient, Scan, User

views = Blueprint('views', __name__)
class_names = ['Glioma','Meningioma','No_Tumor','Pituitary']


model =tf.keras.models.load_model("TUMOR.h5")


def test_on_image(img_path):
	test_image = image.load_img(img_path, target_size=(240,240))
	test_image = image.img_to_array(test_image)
	test_image = test_image.reshape(240, 240, 3)
	test_image = np.expand_dims(test_image, axis=0) 
	result = model.predict(test_image)
	p = max(result.tolist())
	return(class_names[p.index(max(p))])

@views.route('/')
def home():
	return render_template('home.html',user=current_user)

@views.route('/docprofile')
def profile():
	return render_template('docprofile.html',user=current_user)

@views.route('/myProfile')
def patient():
	patient = Patient.query.filter_by(id = current_user.id).first()
	# print(patient.scans)
	# scan = Scan.query.filter_by(user_id = current_user.id).first()
	return render_template('patientprofile.html',user=current_user, patient=patient)


@views.route('/doccard')
def card():
	allusers = User.query.all()
	doctors = []
	for users in allusers:
		if users.role == "Doctor":
			doctors.append(users)
	docDetails = Doctor.query.all()
	return render_template('doccard.html',user=current_user, doctors=doctors, docDetails=docDetails)

app.config['SCAN_UPLOAD'] = 'static/images/uploads/scans'

@views.route('/upload-scan',methods=['POST'])
@login_required
def upload_scan():
	if request.method == 'POST':
		if request.files:
			image = request.files['scan']
			# filename=f'scan-{current_user.name}-{datetime.datetime.now()}{os.path.splitext(image.filename)[1]}'
			# image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD'],secure_filename(filename)))
			# uri = upload_image(image, 'scan')
			basepath = os.path.dirname(__file__)
			file_path=os.path.join(basepath,app.config['SCAN_UPLOAD'],secure_filename(image.filename))
			image.save(file_path)
			preds = test_on_image(file_path)
			print(preds)
			# new_scan = Scan(uri=uri,user_id=current_user.id)
			flash(f'Scan successfully uploaded. {preds}',category='success')
	return redirect(url_for('views.home'))

# def upload_image(image,type):
# 	filename=f'{type}-{current_user.name}-{datetime.datetime.now()}{os.path.splitext(image.filename)[1]}'
# 	image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD'],secure_filename(filename)))
# 	# return f'{app.config["SCAN_UPLOAD"]}/{filename}'
# 	strin = app.config["SCAN_UPLOAD"]+'/'+filename
# 	x=strin.replace('/', '\\')
# 	return x

