from flask import Blueprint, jsonify, request, g
import app.sql.detection_sql as sql
import reco.reco as RR
detection_blueprint = Blueprint('detection_blueprint', __name__)

#检测是否是垃圾邮件
@detection_blueprint.route('/send-mail', methods=['POST'])
def predict_form():
    phoneNumber = g.phone_number
    mail_text = request.json.get('text')
    title = request.json.get('title')
    is_normal = RR.preprocess(mail_text)
    sql.detection(phoneNumber,mail_text,title,is_normal)
    return jsonify({"is_spam": is_normal})
