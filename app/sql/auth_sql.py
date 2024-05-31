from .config import connection
import app.fun.encode as encode

# 查询用户是否存在
def query_user(username):
    cursor = connection.cursor()
    # 编写SQL查询
    query = "SELECT username, password FROM user WHERE phoneNumber=%s"

    # 执行SQL查询
    cursor.execute(query, (username,))

    # 获取所有结果
    result = cursor.fetchone()
    connection.commit()
    cursor.close()
    if result:
        return True
    else:
        return False


# 注册用户
def register_user(username, password, phoneNumber):
    cursor = connection.cursor()
    query = "INSERT INTO user (username, password,phonenumber) VALUES (%s, %s ,%s)"
    cursor.execute(query, (username, password, phoneNumber))
    connection.commit()
    cursor.close()
    return True

#验证用户
def confirm_login(phoneNumber,password):
    cursor = connection.cursor()
    # 编写SQL查询
    query = "SELECT password FROM user WHERE phoneNumber = %s"

    # 执行SQL查询
    cursor.execute(query,(phoneNumber,))

    # 获取所有结果
    stored_hashed_password = cursor.fetchone()
    connection.commit()
    cursor.close()
    # print(password.encode('utf-8'),stored_hashed_password[0].encode('utf-8'))
    if encode.check(password.encode('utf-8'),stored_hashed_password[0].encode('utf-8')):
        return True
    else:
        return False
#更新用户
def update_pass(phoneNumber,password):
    try:
        # 创建游标对象
        cursor = connection.cursor()
        # 编写参数化的UPDATE SQL语句
        query = "UPDATE user SET password = %s WHERE phoneNumber = %s"
        # 执行SQL语句，并传入参数
        cursor.execute(query, (password, phoneNumber))
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
#返回该手机号的用户名
def queryUserName(phoneNumber):
    cursor = connection.cursor()
    query = "SELECT username FROM user WHERE phoneNumber = %s"
    cursor.execute(query, (phoneNumber,))
    result = cursor.fetchone()
    connection.commit()
    cursor.close()
    return result