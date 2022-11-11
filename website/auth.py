from flask import Blueprint, flash, redirect, render_template, request, url_for
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login')
def home():
	date = datetime.now()
	return render_template('login.html', date=date)

@auth.route('/signup')
def signup():
	return render_template('signup.html')