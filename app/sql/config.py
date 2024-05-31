import mysql.connector
from mysql.connector import Error
try:
    # 创建连接
    connection = mysql.connector.connect(
        host='localhost',       # 数据库主机地址
        database='spam',      # 你要连接的数据库名
        user='root',    # 数据库用户名
        password='root' # 用户密码
    )
except Error as e:
    print("error while connecting to MySQL", e)