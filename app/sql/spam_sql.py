
from .config import connection
#查询邮件
def query_spam(phoneNumber,index):
    cursor = connection.cursor()
    query = "SELECT title,text,date,id FROM spam WHERE phoneNumber = %s order by date desc LIMIT 50 OFFSET %s"
    cursor.execute(query, (phoneNumber,index*50))
    content = cursor.fetchall()
    query = "SELECT count(*) FROM spam WHERE phoneNumber = %s"
    cursor.execute(query,(phoneNumber,))
    number = cursor.fetchone()
    connection.commit()
    cursor.close()
    return content,number

#删除邮件
def delete_inbox(table,id):
    cursor = connection.cursor()
    query = "DELETE FROM {} WHERE id = %s".format(table)
    cursor.execute(query,(id,))
    connection.commit()
    cursor.close()
    return True