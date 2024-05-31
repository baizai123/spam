from flask import Blueprint, jsonify, request, g
import app.sql.person_sql as sql
person_blueprint = Blueprint('person_blueprint', __name__)

#修改用户的个人信息
@person_blueprint.route('/SetUser', methods=['post'])
def SetUser():
    userName = request.form.get('username')
    phoneNumber = g.phone_number
    if  request.files.get('file'):
        file = request.files.get('file')
        file.save('./img/'+ phoneNumber +'.jpg')
    return jsonify({'valid':sql.update_user(userName,phoneNumber)})