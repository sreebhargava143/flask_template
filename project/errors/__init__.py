from flask import Blueprint

errors_bp = Blueprint('errors', __name__, template_folder="templates", static_folder="static", static_url_path="/project/errors/static")

def init_app(app):
    handlers.init_error_handler(app)
    app.register_blueprint(errors_bp)

from project.errors import handlers
