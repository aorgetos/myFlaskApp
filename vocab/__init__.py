# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
# from flask.ext.moment import Moment

from .config import config_by_name

bootstrap = Bootstrap()
db = SQLAlchemy()

# Configure authentication
login_man = LoginManager()
login_man.session_protection = "strong"
login_man.login_view = "auth.login"

toolbar = DebugToolbarExtension()

# for displaying timestamps
# moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    login_man.init_app(app)
    bootstrap.init_app(app)
    toolbar.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix = '/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')
    
    from .vocabulary import vocabulary as vocabulary_blueprint
    app.register_blueprint(vocabulary_blueprint, url_prefix = '/vocabulary')
    
    return app
