from flask import Blueprint, jsonify, request, g
import app.sql.spam_sql as sql

spam_blueprint = Blueprint('spam_blueprint', __name__)


# 获取垃圾箱
@spam_blueprint.route('/getSpam', methods=['POST'])
def getSpam():
    # print(request.json)
    phoneNumber = g.phone_number
    index = request.json.get('index')
    content, number = sql.query_spam(phoneNumber, index)
    # print(content,number)
    return jsonify({"content": content, "number": number})


# 删除单个邮件
@spam_blueprint.route('/deleteSpamMail', methods=['post'])
def deteleSpamMail():
    id = request.json.get('id')
    return jsonify({'success_del': sql.delete_inbox('spam', id)})
