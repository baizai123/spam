from flask import g
from flask_jwt_extended import get_jwt_identity

from app import create_app

app = create_app()




if __name__ == '__main__':
    app.run(ssl_context='adhoc')
