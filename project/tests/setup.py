import unittest
import os

from project import create_app, Config
from project.services import db

class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG = False
class TestSetup(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(self.app.config['BASEDIR'], "test_db.db")

        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
