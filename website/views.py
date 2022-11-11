import datetime
import os

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from . import app

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('home.html',user=current_user)

@views.route('/docprofile')
def profile():
	return render_template('docprofile.html',user=current_user)

app.config['SCAN_UPLOAD'] = 'static/images/uploads/scans'

@views.route('/upload-scan',methods=['POST'])
@login_required
def upload_scan():
	if request.method == 'POST':
		if request.files:
			image = request.files['image']
			filename=f'scan-{current_user.name}-{datetime.datetime.now()}.{os.path.splitext(image.filename)[1]}'
			image.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['SCAN_UPLOAD'],secure_filename(filename)))
			
	return redirect(url_for('views.home'))
