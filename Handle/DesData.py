# encoding=utf-8
import base64
import pyDes
import time
from  Handle.handle_init import Handle_init

class EncryptionData:

    def encrypt_data(self,text):
        '''传入参数数据类型为'''
        encrypt_key = "fawmc-count-des-key!#@$%"
        encrypt_iv = "cbc!#@IV"
        if text is None:
            text = ""
            print ("加密字符串为空，请确认数据内容")
            return
        # print ('加密字符串:', text)
        # print ('密钥:', key)
        """实例化加密对象"""
        k = pyDes.triple_des(encrypt_key, pyDes.CBC, IV=encrypt_iv, pad=None, padmode=pyDes.PAD_PKCS5)
        """使用加密方法进行加密"""
        d = k.encrypt(text)
        res = base64.standard_b64encode(d)
        res=str(res,encoding="utf-8")
        # print(res)
        return res
    def decrypt_data(self,text):
        """text参数为bytes类型,返回数据为bytes类型"""
        dencrypt_key = "fawmc-count-des-key!#@$%"
        dencrypt_iv = "cbc!#@IV"
        if text is None:
            text=""
            print("解密字符串为空，请确认数据内容")
            return
        """实例化解密对象"""
        d=pyDes.triple_des(dencrypt_key,pyDes.CBC,IV=dencrypt_iv,pad=None, padmode=pyDes.PAD_PKCS5)
        text=base64.b64decode(text)
        k=d.decrypt(text)
        k=str(k,encoding="utf-8")
        # print(k)
        return k

    def get_token(self):

        token = Handle_init().read_token("token", "login", "test2")
        tt = str(int(time.time() * 1000))
        text = token + '&' + tt
        # print("加密前", text)
        dt=self.encrypt_data(text)
        return dt


if __name__ == "__main__":
    # 获取参数
    '''调试代码'''
    # token=Handle_init().read_token("token","login","test2")
    # tt=str(int(time.time()*1000))
    # text=token+'&'+tt
    text='111111s'
    print("加密前",text)
    dd=EncryptionData()
    dt=dd.encrypt_data(text)
    print("加密后",type(dt))
    print(dt)
    dt=bytes(dt,encoding="utf-8")
    dt='PVwrv7+oVPU='
    print('需要解密的数据',dt)
    print("转换数据类型为bytes",type(dt),dt)
    print("解密后",dd.decrypt_data(dt))
    # print(dd.get_token())
    # print(type(dd.get_token()))
    # dddd={    "Content-Type": "application/json","token":"toke"}
    # print(
    #     'token' in dddd.keys()
    # )