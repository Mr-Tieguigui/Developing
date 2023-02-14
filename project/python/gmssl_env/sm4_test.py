import binascii

#导入国密算法sm4包
from gmssl import sm4

def sm4_encode(key, iv, data):
    """
    国密sm4加密
    :param key: 密钥
    :param data: 原始数据
    :return: 密文hex
    """
    sm4Alg = sm4.CryptSM4()  # 实例化sm4
    sm4Alg.set_key(key.encode(), sm4.SM4_ENCRYPT)  # 设置密钥
    #sm4Alg.set_iv(iv.encode(),sm4.SM4_ENCRYPT)
    dateStr = str(data)
    print("明文:", dateStr)
    enRes = sm4Alg.crypt_cbc(iv.encode(),dateStr.encode())  # 开始加密,bytes类型，ecb模式
    enHexStr = enRes.hex()
    print("密文:", enHexStr)
    return enHexStr # 返回十六进制值
    # return encrypt_value.hex()  

def sm4_decode(key, iv, data):
    """
    国密sm4解密
    :param key: 密钥
    :param data: 密文数据
    :return: 明文hex
    """
    sm4Alg = sm4.CryptSM4()  # 实例化sm4
    sm4Alg.set_key(key.encode(), sm4.SM4_DECRYPT)  # 设置密钥
    #sm4Alg.set_iv(iv.encode(),sm4.SM4_DECRYPT)
    deRes = sm4Alg.crypt_cbc(iv.encode(),bytes.fromhex(data))  # 开始解密。十六进制类型,ecb模式
    deHexStr = deRes.decode()
    print("解密后明文:", deRes)
    print("解密后明文hex:", deHexStr)
    return deHexStr

#测试函数
def test(key, iv , strData):
    # key = "E1A90FB64DDE12AE";  
    # iv = "E1A90FB64DDE12AE"
    # strData = "12345abcde"

    enHexRes = sm4_encode(key,iv,strData)

    print("解密测试===",enHexRes)

    sm4_decode(key,iv,enHexRes)

# main 
if __name__ == '__main__':
    print("main begin")
    key = input("key:\n")
    iv = input("iv:\n")
    data = input("data:\n")
    test(key, iv, data)
    input('Press Enter to exit…')
