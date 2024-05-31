from flask import Blueprint
from .auth import auth_blueprint
from .detection import detection_blueprint
from .inbox import inbox_blueprint
from .index import index_blueprint
from .person import person_blueprint
from .spam import spam_blueprint
from .chart import chart_blueprint
def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(detection_blueprint)
    app.register_blueprint(inbox_blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(person_blueprint)
    app.register_blueprint(spam_blueprint)
    app.register_blueprint(chart_blueprint)