from flask import Blueprint, jsonify, request, g
import app.sql.chart_sql as sql
chart_blueprint = Blueprint('chart_blueprint', __name__)

#正常邮件和垃圾邮件的数目
@chart_blueprint.route('/getCount', methods=['POST'])
def getCount():
    phoneNumber = g.phone_number
    spamCount,inboxCount = sql.count_phone_number(phoneNumber)
    return jsonify({'spamCount':spamCount,'inboxCount':inboxCount})