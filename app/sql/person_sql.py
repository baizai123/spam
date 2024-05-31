from .config import connection
#更新该用户的用户名
def update_user(username, phoneNumber):
    try:
        # 创建游标对象
        cursor = connection.cursor()
        # 编写参数化的UPDATE SQL语句
        query = "UPDATE user SET username = %s WHERE phoneNumber = %s"
        # 执行SQL语句，并传入参数
        cursor.execute(query, (username, phoneNumber))
        # 提交事务
        connection.commit()
        # print("Username updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        # 如果有异常，回滚事务
        connection.rollback()
    finally:
        # 关闭游标
        cursor.close()
    return True