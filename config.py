import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    BASEDIR = basedir
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'project.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    APP_SYSTEM_ERROR_SUBJECT_LINE = os.environ.get("APP_SYSTEM_ERROR_SUBJECT_LINE")

    ADMINS = [os.environ.get("ADMIN")]
    

