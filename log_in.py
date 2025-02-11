import argon2
from pathlib import Path
import json

# 创建 Argon2 实例
ph = argon2.PasswordHasher()

# 存储用户信息的文件路径
users_db_path = Path("users.json")

def verify_password(hashed_password: str, password_to_check: str) -> bool:
    """验证密码是否匹配"""
    try:
        ph.verify(hashed_password, password_to_check)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

def login_user(username: str, password: str) -> bool:
    """验证用户登录"""
    if not users_db_path.exists():
        raise FileNotFoundError("用户数据库不存在")

    with users_db_path.open('r', encoding='utf-8') as f:
        users_db = json.load(f)

    # 获取存储的哈希密码
    hashed_password = users_db.get(username)

    if hashed_password is None:
        raise ValueError("用户名不存在")

    # 验证密码
    if verify_password(hashed_password, password):
        print("登录成功")
        return True
    else:
        print("密码错误")
        return False

# 示例：用户登录
login_user("洛天衿", "752193577")  # 输出: 登录成功