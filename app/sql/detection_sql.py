import datetime
from .config import connection

#保存检测内容
def detection(phoneNumber,text,title,is_normal):#is_normal判断是否为正常邮件
    cursor = connection.cursor()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    if title=='':
        title = '无标题'
    if is_normal:
        query = "INSERT INTO inbox (phoneNumber, title,text ,date) VALUES (%s, %s,%s,%s)"
    else:
        query = "INSERT INTO spam (phoneNumber, title,text ,date) VALUES (%s, %s,%s,%s)"
    cursor.execute(query,(phoneNumber,title,text,current_time))
    connection.commit()
    cursor.close()