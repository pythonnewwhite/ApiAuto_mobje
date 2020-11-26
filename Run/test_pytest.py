# coding=utf-8
# import unittest
import pytest
# import pytest_html
import json
# import os

from Handle.handle_json import Handel_json
from Handle.handle_init import Handle_init
from Handle.handle_excel import Handle_Excel
from Base.base_request import BaseRquest
from Handle.DesData import EncryptionData

hd_ini=Handle_init()
hd_ex = Handle_Excel()
data=hd_ex.liat_totuple(1)

@pytest.mark.parametrize('case_data1',data)
class Test_pytest(object):
    re=BaseRquest()
    @pytest.mark.flaky(returns=1)
    def test_runcase(self,case_data1):
        self.my_case(case_data1)
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
    # pytest.main(['-s --runs 1','test_pytest.py','--alluredir=../Report/xml'])
    # os.system(' cd C:\soft\Pycharm\workspace\new_mojie> allure generate reports --clean')
    pytest.main(['--reruns','4','test_pytest.py','--html=../Report/mojie.html'])
    # pytest.main(['-s','test_pytest.py','--junit-xml=../Report/report_name.xml'])