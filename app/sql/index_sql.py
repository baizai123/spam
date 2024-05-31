from .config import connection
#模糊查询邮件（通过内容和标题）
def query_mail(pageIndex,searchData,phoneNumber):
    cursor = connection.cursor()
    if(pageIndex=='spam'):
        query = "SELECT title,text,date,id FROM spam WHERE (title LIKE %s OR text LIKE %s) AND phoneNumber = %s ORDER BY date DESC;"
        query1 = "SELECT count(*) FROM spam WHERE (title LIKE %s OR text LIKE %s) AND phoneNumber = %s ORDER BY date DESC;"
    elif(pageIndex=='inbox'):
        query = "SELECT title,text,date,id FROM  inbox WHERE (title LIKE %s OR text LIKE %s) AND phoneNumber = %s ORDER BY date DESC;"
        query1 = "SELECT count(*) FROM  inbox WHERE (title LIKE %s OR text LIKE %s) AND phoneNumber = %s ORDER BY date DESC;"
    searchData1 = "%{}%".format(searchData)
    cursor.execute(query,(searchData1,searchData1,phoneNumber))
    content = cursor.fetchall()
    cursor.execute(query1,(searchData1,searchData1,phoneNumber))
    number = cursor.fetchone()
    connection.commit()
    cursor.close()
    return content,number