

"""
1   /user/2   加密后    /user/aswed

通过加密方法
get_secret_text(1)

requests.gets(url)

"""
import time
from base64 import b64encode

import rsa

# ----先导入rsa库


#加密数据；时间戳和token
def get_sign(ts,token):
    #1 准备明文

    s=token[:50] +str(ts)
    # 2 准备好密钥

    key='-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE\nO3F7g s+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr\ntuPorOc42+gLnFfyhJAw dZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S\nkKlZFc8Br7SHtbL2tQIDAQAB\n-----END PUBLIC KEY-----\n'

    #3 调用加密模块提供的加密方法

    public_key=rsa.PublicKey.load_pkcs1_openssl_pem(key.encode())   #获取加密密钥方法

    enctypred=rsa.encrypt(s.encode(),public_key)

    return b64encode(enctypred).decode()   #导入b64方法


ts=int(time.time())  #整数时间戳
print(ts)

token='asjdkjjkafjkdjkjkfjkdsjkjewicdjkclqldcoirjkenzcjksjkdfmweuefdasjkdiqokewrjqei9riklejdueuwrjkwjwuwes8qj'

s=get_sign(ts,token)

print(s)