from flask import Blueprint

mini_app1_bp = Blueprint('mini_app1', __name__, template_folder="templates", static_url_path="/project/mini_app1/static", static_folder="static")

def init_app(app):
    app.register_blueprint(mini_app1_bp)

from project.mini_app1 import routes