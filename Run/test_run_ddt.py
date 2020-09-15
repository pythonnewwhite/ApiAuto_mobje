# coding=utf-8
import unittest
import ddt
import json

from Handle import handle_json
from Handle import handle_init
from Handle import handle_excel
from Base import base_request

@ddt.ddt
class RunDdt(unittest.TestCase):
    hd_ex = handle_excel.Handle_Excel()
    data = hd_ex.get_row_values()
    hd_ini=handle_init.Handle_init()
    hd_js=handle_json.Handel_json()
    re=base_request.BaseRquest()
    @ddt.data(*data)
    def test_case(self,data):
        cookie=None
        header=None
        '''
        1、判断是否执行用例
        2、读取配置文件中的域名（ini）、读取配置文件的地址（Excel）
            拼接url
        2、判断是否有依赖参数---data
            读取配置文件--key&value
            更新data
        3、判断是否有依赖参数---header
            读取配置文件--key&value
            更新data
        4、判断是否有依赖参数---cookie
            读取配置文件--key&value
            更新data
        5、判断请求方式---get&post
        6、判断是否有被依赖参数
            写入到配置文件中（ini）
        '''
        if data[2] == 'yes':
            """1、从Excel表中读取IsRun (data[2])字段判断是否执行用例
                1.1、值为yes 时，执行此条用例
                1.2、值不为yes时，不执行此条用例"""
        # 2、读取接口、域名和路径进行拼接（ini文件的host+Excel文件的接口路径）
            url=self.hd_ini.read_ini("host","test1")+data[9]
            # print("url:",url)
            # print(type(path))
        else:
            print("本条case不执行")
            return
        if data[3] != None:
            '''1、从Excel中读取relation_data_option、relation_data_key，判断params&body 参数是否有依赖
                    1.1、有依赖，从ini文件中读取依赖参数对应的值
                    1.2、无依赖，从Excel读取data参数对应的值
            '''
            relation_data_option = data[3]  # 获取列表中的data数据中关联数据的key
            relation_data=self.hd_ini.read_ini(relation_data_option,"test1")   #获取ini文件中的关联数据
            relation_data_key=data[6]   #获取data数据中关联数据的key
            # 3、从Excel 表格读取data 信息，data 需要传输str类型
            relation_data_value =self.hd_js.get_json_value(data[14],relation_data_key)  # 获取关联key对应的value
            """调用函数，将关联参数-关联参数value填充到读取的data中，返回新的data"""
            get_params = eval(data[11])  # 获取需要传递的data参数
            get_params = self.hd_js.change_json_value(get_params,relation_data_key ,relation_data_value)  # 将获取的value填充到data参数中
        else:
            # get_params = eval(data[11])
            get_params=data[11]
            # print(type(get_params))
            # print("data",type(get_params))
        if data[4] != None:
            '''取header参数
            1、判断headers中是否有关联key
                1.1、有关联，根据 relation_header_option、relation_header_key，
                    从ini文件中读取关联参数对应值，返回完整的header
                1.2、无关联，直接取Excel中的 header参数'''
            relation_header_option=data[4]
            relation_header_key=data[7]
            relation_header_data=json.loads(self.hd_ini.read_ini(relation_header_option,"test1"))

            relation_header_value=self.hd_js.get_json_value(relation_header_data,relation_header_key)
            header_old = json.loads(data[13])  # 获取header数据
            header=self.hd_js.change_json_value(header_old,relation_header_key,relation_header_value)
        else:
            header = eval(data[13])
            # print("header",type(header))
        if data[10] != None:
            print(data[0]+data[1])
            # print("header;", header)
            '''1、从Excel中读取的 method(data[10])参数判断请求方式；
                    1.1、get请求走get方法，参数params 为字典格式，header为字典格式
                    1.2、post请求走post方法，参数body 为str格式，header为字典格式
                    1.3、请求方式为空，打印日志，请求方法为空'''
            if data[10] == "post":
                # get_params=str(get_params)
                print("这个是post请求")
                re = self.re.send_post(url=url, data=get_params, cookie=cookie, header=header)
                re_response = json.loads(re.text)
                self.assertEqual(re_response["status"],"SUCCESS")
                # if re.status_code == 200:
                #     print("code_pass:",re.status_code)
                # if re_response["status"] is "SUCCESS":
                #     print("status:",re_response["status"])
                # else:
                #     print(re_response)
                if data[14]!=None:
                    self.hd_ini.write_ini(data[14],re.text)

            elif data[10] == 'get':
                print("这个是get请求")
                get_params=eval(get_params)
                re = self.re.send_get(url=url, data=get_params, cookies=cookie, headers=header)
                re_response = json.loads(re.text)
                self.assertEqual(re.status_code,200)
                self.assertEqual(re_response["status"],"SUCCESS")
                # if re.status_code == 200:
                #     print("code_pass")
                #     print(re.text)
                # else:
                #     print(re.text)


    def setUp(self):
        pass
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()