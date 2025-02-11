import argon2
from pathlib import Path
import json

# 创建 Argon2 实例
ph = argon2.PasswordHasher()

# 存储用户信息的文件路径
users_db_path = Path("users.db")

def register_user(username: str, password: str):
    """注册新用户"""
    if users_db_path.exists():
        with users_db_path.open('r', encoding='utf-8') as f:
            users_db = json.load(f)
    else:
        users_db = {}

    # 检查用户名是否已存在
    if username in users_db:
        raise ValueError("用户名已存在")

    # 哈希主密码
    hashed_password = ph.hash(password)

    # 存储用户信息
    users_db[username] = hashed_password

    # 写入文件
    with users_db_path.open('w', encoding='utf-8') as f:
        json.dump(users_db, f, ensure_ascii=False, indent=4)

# 示例：注册用户
register_user("星乃凛", "752193577")