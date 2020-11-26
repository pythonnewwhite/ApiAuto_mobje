# coding=utf-8
import os
import sys
import requests
import json

from DesData import EncryptionData
from Handle.handle_excel import Handle_Excel
from Handle.handle_init import Handle_init
from handle_json import Handel_json

hd_ini=Handle_init()
hd_ex = Handle_Excel()
data=hd_ex.liat_totuple(1)

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

    def my_case(self,case_data):
        print(case_data)
        cookie=None
        header=None
        body=None
        if case_data[2] == 'yes':
            if hd_ini.read_ini("host", "test2") is not None:
                host=eval(hd_ini.read_ini("host","test2"))
            print("host",type(host))
            path=case_data[3]
            url=host+path
            print("url:",url)
        else:
            print("本条case不执行")
            return
        if case_data[7] !=None:
            print(case_data[7])
            header=eval(case_data[7])
            print("header",type(header))
            if 'token' in header.keys() :
                new_token=EncryptionData().get_token()
                header=Handel_json().change_json_value(header,'token',new_token)
        else:
            print("header为空")

        if case_data[4] == "post":
                print("这个是post请求")
                body=case_data[5]
                if case_data[6] != None:
                    cookie=eval(case_data[6])
                # if case_data[7] !=None:
                #     header=eval(case_data[7])
                print("header", type(header))
                print("body", type(body))
                print(body,header,cookie)
                res = self.re.send_post(url=url, data=body, cookie=cookie, header=header)
                if res.text !="" and case_data[1]=="密码登录-正确":
                    re_response = json.loads(res.text)
                    # print("reeee",type(re_response),re_response["status"])
                    if re_response["status"] == "success":
                        print(111111111111)
                        Handle_init().write_ini("login",res.text,section="test2")
                        print(2222222222222)
                    else:
                        return
                elif res.text !="":
                    re_response = json.loads(res.text)
                    assert re_response['status']=='success'
                assert res.status_code==200

                row=int(case_data[0][-3])*100+int(case_data[0][-2])*10+int(case_data[0][-1])+1
                print("-------------------------------",row)
                Handle_Excel().excel_write_data(row=row,cols=11,value=res.text)
                print(res.text)
        elif case_data[4] == 'get':
                print("这个是get请求")
                get_params=eval(case_data[5])
                # print(header)
                res = BaseRquest().send_get(url=url, data=get_params, cookies=cookie, headers=header)
                if res.text !="":
                    re_response = json.loads(res.text)
                    assert re_response['status'] == "success"
                else:
                    return
                assert res.status_code==200

                row=int(case_data[0][-3])*100+int(case_data[0][-2])*10+int(case_data[0][-1])+1
                print("-------------------------------",row)
                Handle_Excel().excel_write_data(row=row,cols=11,value=res.text)
                print(res.text)



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
