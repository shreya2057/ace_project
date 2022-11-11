from os import path

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fagsdfbaisdfkbdjkgn'
    from .auth import auth
    from .views import views
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app
