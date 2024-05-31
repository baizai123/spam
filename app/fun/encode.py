import bcrypt
def encode(password):
    # 要散列的密码
    password = password.encode("utf-8")

    # 生成盐
    salt = bcrypt.gensalt()

    # 创建密码的散列值
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password
def check(password, stored_hashed_password):
    return bcrypt.checkpw(password, stored_hashed_password)