from os import path
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fagsdfbaisdfkbdjkgn'

    @app.route('/')
    def function():
        return render_template('base.html')

    return app

