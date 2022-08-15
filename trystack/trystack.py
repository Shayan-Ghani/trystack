from json import load as json_load
from flask import Blueprint, Flask
from flask_restful import Api 

from .config import Config

apiv1_bp = Blueprint(name="apiv1_bp", import_name=__name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp) 
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config)
    if config_file is not None:
        app.config.from_file(config_file , load=json_load)
    app.register_blueprint(apiv1_bp) # Register /api/v1 blueprint to main application
    
    return app
