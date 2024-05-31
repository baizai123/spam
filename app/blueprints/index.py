from flask import Blueprint, jsonify, request, send_from_directory, g
import app.sql.index_sql as sql

index_blueprint = Blueprint('index_blueprint', __name__)


# 模糊搜索
@index_blueprint.route('/Search', methods=['POST'])
def search():
    # 选择是什么样式的邮件
    pageIndex = request.json.get('pageindex')
    # 搜索框的内容
    searchData = request.json.get('searchdata')
    phoneNumber = g.phone_number
    content, number = sql.query_mail(pageIndex, searchData, phoneNumber)
    return jsonify({"content": content, 'number': number})


# 返回头像
@index_blueprint.route('/images')
def get_image():
    return send_from_directory('../img', g.phone_number+'.jpg')
