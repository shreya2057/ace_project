from flask import Blueprint, flash, redirect, render_template, request, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login')
def home():
	return render_template('login.html')