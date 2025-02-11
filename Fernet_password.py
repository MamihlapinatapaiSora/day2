from cryptography.fernet import Fernet

def load_key():
    """加载密钥"""
    return open("secret.key", "rb").read()

# 加载密钥
key = load_key()
cipher_suite = Fernet(key)

def encrypt_message(message: str) -> bytes:
    """加密消息"""
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# 示例：加密一条消息
message = "星乃凛"
encrypted_message = encrypt_message(message)
print("加密后的消息:", encrypted_message)

def decrypt_message(encrypted_message: bytes) -> str:
    """解密消息"""
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# 示例：解密消息
decrypted_message = decrypt_message(encrypted_message)
print("解密后的消息:", decrypted_message)