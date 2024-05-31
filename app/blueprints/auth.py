import random
from flask import Blueprint, jsonify, request, session, app, g
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import app.sql.auth_sql as sql
import app.fun.encode as encode
import app.extensions as ex
import app.fun.code as code
from datetime import timedelta
auth_blueprint = Blueprint('auth_blueprint', __name__)


# 注册路由
@auth_blueprint.route('/register', methods=['post'])
def register():
    userName = request.json.get('username')
    password = request.json.get('password')
    phoneNumber = request.json.get('phoneNumber')
    hashed_password = encode.encode(password)
    if sql.query_user(phoneNumber):
        return jsonify({'message': "该手机号已被使用！"})
    if sql.register_user(userName, hashed_password, phoneNumber):
        return jsonify({'valid': True})


# 登录验证路由，会授予token
@auth_blueprint.route('/confirm', methods=['POST'])
def confirm():
    access_token = ''
    phoneNumber = request.json.get('phoneNumber')
    password = request.json.get('password')
    if sql.confirm_login(phoneNumber, password):
        access_token = create_access_token(identity=phoneNumber,expires_delta=timedelta(minutes=15))
    return jsonify({'valid': sql.confirm_login(phoneNumber, password), 'access_token': access_token,
                    'username': sql.queryUserName(phoneNumber)})


# 发送验证码
@auth_blueprint.route('/SendCode', methods=['post'])
def SendCode():
    phoneNumber = request.json.get('phoneNumber')
    if sql.query_user(phoneNumber):

        random_code = str(random.randint(1000, 9999))
        code.Sample.main([phoneNumber,random_code])
        # 保存验证码到Redis，key为phoneNumber，value为验证码，过期时间300秒
        ex.r.setex(phoneNumber, 300, random_code)
        return jsonify({'valid': True})
    return jsonify({'valid': False})


# 验证验证码，修改该手机号的密码
@auth_blueprint.route('/VerifyCode', methods=['POST'])
def VerifyCode():
    phoneNumber = request.json.get('phoneNumber')
    input_code = request.json.get('code')  # 用户输入的验证码
    password = request.json.get('password')
    # 从Redis获取验证码
    real_code = ex.r.get(phoneNumber)
    hashed_password = encode.encode(password)
    if real_code and real_code.decode('utf-8') == input_code:
        ex.r.delete(phoneNumber)  # 立即删除已验证的键值对
        sql.update_pass(phoneNumber, hashed_password)
        # 验证码匹配
        return jsonify({'valid': True})
    else:
        # 验证码不匹配或已过期
        return jsonify({'valid': False, 'message': 'Invalid or expired code.'})

#路由验证
@auth_blueprint.route('/protected', methods=['GET'])
@jwt_required()  # 使用此装饰器保护路由，要求调用此端点的请求携带有效的 JWT
def protected():
    current_user = get_jwt_identity()  # 获取携带JWT的用户的身份
    g.phoneNumber = current_user
    return jsonify(logged_in_as=current_user), 200

