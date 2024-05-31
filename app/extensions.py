import secrets

import redis
from flask_cors import CORS
from flask_jwt_extended import JWTManager

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def init_extensions(app):
    CORS(app, resources=r'/*', supports_credentials=True)
    app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)  # 生成一个32字节长度的随机十六进制字符串
    secret_key = secrets.token_urlsafe(16)
    app.secret_key = secret_key
    jwt = JWTManager(app)  # 初始化JWTManager并绑定到Flask应用


    # 连接到本地Redis实例
