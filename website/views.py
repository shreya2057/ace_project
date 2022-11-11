from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('home.html',user=current_user)

@views.route('/docprofile')
def profile():
	return render_template('docprofile.html',user=current_user)