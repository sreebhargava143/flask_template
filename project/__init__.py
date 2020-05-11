'''
Module to make vishrambh_app as a package
'''
from flask import Flask, session, flash, redirect, url_for
from datetime import datetime

from config import Config

def create_app(config_class=Config):
    '''
    Factory pattern to create different app instances
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from project import services, mini_app1, errors
    services.init_app(app)
    mini_app1.init_app(app)
    errors.init_app(app)
    
    @app.after_request
    def after_request(response):
        '''Resolving back button bug after logout'''
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response

    return app

