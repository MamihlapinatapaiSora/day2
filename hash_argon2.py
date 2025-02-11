import argon2

# 创建 Argon2 实例
ph = argon2.PasswordHasher()

# 用户输入的主密码
master_password = "752193577"

# 哈希主密码
hashed_password = ph.hash(master_password)

# 打印哈希后的密码（仅用于演示，实际应用中不要直接打印哈希值）
#print("哈希后的密码:", hashed_password)

def verify_password(hashed_password: str, password_to_check: str) -> bool:
    """验证密码是否匹配"""
    try:
        ph.verify(hashed_password, password_to_check)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

# 示例：验证密码
password_to_check = "752193577"
is_valid = verify_password(hashed_password, password_to_check)
print("密码是否有效:", is_valid)