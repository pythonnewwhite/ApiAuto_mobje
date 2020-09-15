# coding=utf-8
import os
import sys
import requests
import json
from Handle import handle_excel
from Handle.handle_init import Handle_init
class BaseRquest:
    def __init__(self):
        pass
    def send_post(self,url,data,cookie=None,header=None):
        """"""
        res=requests.post(url=url,data=data,cookies=cookie,headers=header)
        return res

    def send_get(self,url,data,cookies=None,headers=None):
        """"""
        res=requests.get(url=url,params=data,cookies=cookies,headers=headers)
        return res

if __name__ == '__main__':
    re=BaseRquest()
    HI=Handle_init()
    host=HI.read_ini(key="host",node="test2")
    host=eval(host)
    print(host is not None)
    print("host",type(host),host)
    url1="http://mgtportal-tc-uat.mobje.faw-vw.com/tsl/api/"
    url2="user/user/enrollee/login/password"
    # url=.join(host,url2)
    url='{}{}'.format(host,url2)
    print("url",type(url),url)
    print(sys.path)
    # header={'Content-Type': 'application/json;charset=utf-8'}
    # cookie=None
    # data={"phone":"3b8olyAWSNaWVpXe0VFqeg==","password":"PVwrv7+oVPU="}
    # data=json.dumps(data)
    # print(type(data))
    # data=None
    # re = re.send_post(url=url, data=data, header=header, cookie=cookie)
    # print(re.status_code)
    # print(type(re.text))
    # print(re.text)
    # print(re.text == "")
