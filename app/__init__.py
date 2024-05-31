from flask import Flask, g
from flask_jwt_extended import get_jwt_identity

from .extensions import init_extensions
from .blueprints import register_blueprints  #

def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request_func():
        # if get_jwt_identity():
        #     g.phone_number = get_jwt_identity()
        #     print(g.phone_number)
        g.phone_number = '15255949233'
    # app.config.from_object(config_filename)
    init_extensions(app)
    register_blueprints(app)



    return app
