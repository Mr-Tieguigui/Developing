# gmssl部分
SM2属于非对称加密算法，使用公钥加密，私钥解密，在安全性和运算速度方面要优于RSA算法。
SM3属于不可逆加密算法，类似于md5，常用于签名。
SM4属于对称加密算法，可用于替代DES/AES等国际算法， SM4算法与AES算法具有相同的密钥长度和分组长度，都是128位。
## 1. sm3_test.py
## 2. sm4_test.py
## 未完待续....

# pycryptodome [项目网址]https://github.com/Legrandin/pycryptodome
## 初试
### SHA256 计算散列值（哈希值）
```python
# SHA256.py
from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update('message'.encode())
print(hash.digest())
# b'\xabS\n\x13\xe4Y\x14\x98+y\xf9\xb7\xe3\xfb\xa9\x94\xcf\xd1\xf3\xfb"\xf7\x1c\xea\x1a\xfb\xf0+F\x0cm\x1d'
```

### 公钥
公钥系统下，发送方和接收方使用不同密钥——公钥或私钥。
```python
# Key_genarate.py
from Crypto.PublicKey import RSA
key_pair = RSA.generate(4096)  # 生成密钥对
open('public.pem', 'wb').write(key_pair.public_key().export_key('PEM'))  # 导出公钥
open('private.pem', 'wb').write(key_pair.export_key('PEM'))  # 导出私钥
```
## 加解密
`三种加密方式：`
- 对称加密：参与方使用相同密钥进行加解密，速度快，适合处理大量数据。如 AES。
- 非对称加密：发送方使用公钥加密，接收方使用私钥解密，速度慢。如 RSA。
- 混合加密：将上述加密进行组合，优点兼具，非对称加密用于保护有效时间短的对称密钥，对称加密用于加密实际数据。

### 对称加密
两种对称加密方式：
- 流加密：一次加密一个字节数据。如 ChaCha20、XChaCha20 和 Salsa20
- 分组密码：对固定数量的数据进行加密。如 AES，一次加密 16 个字节。
#### Salsa20 加密
```python
# Salsa20.py
from Crypto.Cipher import Salsa20

# 加密方
plaintext = b'Hello World!'  # 明文
key = b'0123456789012345'  # 密钥
cipher = Salsa20.new(key=key)
msg = cipher.nonce + cipher.encrypt(plaintext)  # 消息=随机数+密文

# 解密方
key = b'0123456789012345'  # 密钥
msg_nonce = msg[:8]
ciphertext = msg[8:]
cipher = Salsa20.new(key=key, nonce=msg_nonce)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
# b'Hello World!'
```
#### AES 加密
```python
# AES_CBC.py
from Crypto.Cipher import AES

# 加密方
plaintext = b'Hello World!'  # 明文
key = b'0123456789012345'  # 密钥
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# 解密方
key = b'0123456789012345'  # 密钥
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)  # 验证真实性
    print(plaintext)
except ValueError:
    print('密钥不正确或消息被破坏')
```

### 非对称加密
#### RSA 加密
```python
# RSA.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成公私密钥
key_pair = RSA.generate(1024)
open('public.pem', 'wb').write(key_pair.public_key().export_key('PEM'))
open('private.pem', 'wb').write(key_pair.export_key('PEM'))

# 加密方
plaintext = b'Hello World!'
public_key = RSA.importKey(open('public.pem').read())
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(plaintext)

# 解密方
private_key = RSA.importKey(open('private.pem').read())
cipher = PKCS1_OAEP.new(private_key)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
```
`实际场景下，密钥长度应使用 3072 或 4096 位`

## 数字签名
用于保证完整性和不可抵赖性。

### PKCS#1 RSA 签名
```python 
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

# 生成公私密钥
key_pair = RSA.generate(1024)
open('public.pem', 'wb').write(key_pair.public_key().export_key('PEM'))
open('private.pem', 'wb').write(key_pair.export_key('PEM'))

# 发送方
plaintext = b'Hello World!'
private_key = RSA.importKey(open('private.pem').read())
signer = pkcs1_15.new(private_key)
hash = SHA256.new(plaintext)
signature = signer.sign(hash)

# 接收方
plaintexts = [b'Hello World!', b'abc']
public_key = RSA.importKey(open('public.pem').read())
signer = pkcs1_15.new(public_key)
for plaintext in plaintexts:
    hash = SHA256.new(plaintext)
    try:
        signer.verify(hash, signature)
        print('合法')
    except:
        print('非法')
```

## 哈希函数
`用于信息摘要。`
将任意二进制字符串作为输入，并产生类似随机的固定长度的输出，即摘要或哈希值。

### SHA256 计算散列值（哈希值）
```python
from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update('message'.encode())
print(hash.digest())
# b'\xabS\n\x13\xe4Y\x14\x98+y\xf9\xb7\xe3\xfb\xa9\x94\xcf\xd1\xf3\xfb"\xf7\x1c\xea\x1a\xfb\xf0+F\x0cm\x1d'
```
## 安全通信
### PBKDF2 进行口令保护
```python
from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

password = '123456'  # 口令
salt = get_random_bytes(16)  # 加盐
keys = PBKDF2(password, salt, 64, count=1000000, hmac_hash_module=SHA512)
key1 = keys[:32]
key2 = keys[32:]
```


# [cryptography](https://cryptography.io/en/latest/)