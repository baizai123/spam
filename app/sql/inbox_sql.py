from .config import connection
#降序查询邮件
def query_inbox(phoneNumber,index):
    cursor = connection.cursor()
    query = "SELECT title,text,date,id FROM inbox WHERE phoneNumber = %s order by date desc LIMIT 50 OFFSET %s"
    cursor.execute(query, (phoneNumber,index*50))
    content = cursor.fetchall()
    query = "SELECT count(*) FROM inbox WHERE phoneNumber = %s"
    cursor.execute(query,(phoneNumber,))
    number = cursor.fetchone()
    connection.commit()
    cursor.close()
    return content,number

#删除单个邮件
def delete_inbox(table,id):
    cursor = connection.cursor()
    query = "DELETE FROM {} WHERE id = %s".format(table)
    cursor.execute(query,(id,))
    connection.commit()
    cursor.close()
    return True
#删除所有邮件
def delete_all_mail(table,allMailId):
    cursor = connection.cursor()
    format_strings = ','.join(['%s'] * len(allMailId))
    query = "DELETE FROM {} WHERE id IN ({})".format(table, format_strings)
    cursor.execute(query, tuple(allMailId))
    connection.commit()
    cursor.close()
    return True