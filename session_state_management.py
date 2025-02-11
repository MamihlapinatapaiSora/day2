import secrets
import time

# 存储会话令牌的字典
sessions = {}

def generate_session_token(username: str) -> str:
    """生成会话令牌"""
    token = secrets.token_urlsafe(32)#生成一个 URL 安全的随机令牌
    sessions[token] = {
        "username": username,
        "timestamp": time.time()
    }#将令牌作为键，用户名和当前时间戳作为值存储在 sessions 字典中。
    return token

def validate_session_token(token: str) -> bool:
    """验证会话令牌"""
    session = sessions.get(token)
    if session is None:
        return False

    # 检查会话是否过期（例如，设置为1小时有效期）
    if time.time() - session["timestamp"] > 3600:
        del sessions[token]
        return False

    return True

def logout_user(token: str):
    """注销用户"""
    if token in sessions:
        del sessions[token]

# 示例：生成会话令牌
token = generate_session_token("洛天衿")
print("生成的会话令牌:", token)

# 示例：验证会话令牌
is_valid = validate_session_token(token)
print("会话令牌是否有效:", is_valid)  # 输出: 会话令牌是否有效: True

# 示例：注销用户
logout_user(token)
is_valid_after_logout = validate_session_token(token)
print("会话令牌是否有效（注销后）:", is_valid_after_logout)  # 输出: 会话令牌是否有效（注销后）: False