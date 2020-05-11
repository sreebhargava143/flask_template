from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
moment = Moment()
csrf_protect = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    bootstrap.init_app(app)
    moment.init_app(app)
    csrf_protect.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()