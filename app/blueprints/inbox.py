from flask import Blueprint, jsonify, request,session,g
from flask_jwt_extended import get_jwt_identity, jwt_required

import app.sql.inbox_sql as sql

inbox_blueprint = Blueprint('inbox_blueprint', __name__)


# 获取正常邮件
@inbox_blueprint.route('/getInbox', methods=['POST'])
def getInbox():
    phoneNumber = g.phone_number
    index = request.json.get('index')
    content, number = sql.query_inbox(phoneNumber, index)
    return jsonify({"content": content, "number": number})


# 删除单个邮件
@inbox_blueprint.route('/deleteInboxMail', methods=['post'])
def deteleInboxMail():
    id = request.json.get('id')
    return jsonify({'success_del': sql.delete_inbox('inbox', id)})

# 删除所选的邮件
@inbox_blueprint.route('/deleteAllMail', methods=['post'])
def deleteAllMail():
    table = request.json.get('table')
    if table != 'inbox' and table != 'spam':
        return jsonify({''})
    allMailId = request.json.get('allMailId')
    return jsonify({'success_del':sql.delete_all_mail(table,allMailId)})