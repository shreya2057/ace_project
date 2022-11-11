from flask import Blueprint, flash, redirect, render_template, request, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('home.html')

@views.route('/docprofile')
def profile():
	return render_template('docprofile.html')