import json
from cryptography.fernet import Fernet

# 生成密钥并保存到文件
def generate_and_save_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# 加载密钥
def load_key():
    return open("secret.key", "rb").read()

# 加密消息
def encrypt_message(cipher_suite, message: str) -> bytes:
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# 解密消息
def decrypt_message(cipher_suite, encrypted_message: bytes) -> str:
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# 保存加密数据到 JSON 文件
def save_encrypted_data_to_json(data_dict, file_path):
    # 加载密钥
    key = load_key()
    cipher_suite = Fernet(key)

    # 加密每个值
    encrypted_data = {k: encrypt_message(cipher_suite, v) for k, v in data_dict.items()}

    # 将加密数据转换为 base64 编码的字符串以便存储在 JSON 中
    encoded_data = {k: v.decode('utf-8') for k, v in encrypted_data.items()}

    # 写入 JSON 文件
    with open("test_json", 'w', encoding='utf-8') as f:
        json.dump(encoded_data, f, ensure_ascii=False, indent=4)

# 从 JSON 文件加载加密数据
def load_encrypted_data_from_json(file_path):
    # 加载密钥
    key = load_key()
    cipher_suite = Fernet(key)

    # 读取 JSON 文件
    with open("test_json", 'r', encoding='utf-8') as f:
        encoded_data = json.load(f)

    # 解码 base64 字符串并解密每个值
    decrypted_data = {}
    for k, v in encoded_data.items():
        encrypted_bytes = v.encode('utf-8')
        decrypted_value = decrypt_message(cipher_suite, encrypted_bytes)
        decrypted_data[k] = decrypted_value

    return decrypted_data

# 示例数据
data_dict = {
    "username": "星乃凛",
    "password": "752193577"
}

generate_and_save_key()#生成密钥
# 保存加密数据到 JSON 文件
save_encrypted_data_to_json(data_dict, "secrets.json")

# 从 JSON 文件加载加密数据
loaded_data = load_encrypted_data_from_json("secrets.json")
print("加载的数据:", loaded_data)