#coding=utf-8
import ddt
import unittest
import os
import HTMLTestRunner
from Handle import handle_excel,handle_json,handle_init
from Base import base_request


class RunCases(unittest.TestCase):

    def test_run(self):
        test_case = handle_excel.Handle_Excel()
        sheet_name = test_case.get_sheet_data(0)
        hd_ini = handle_init.Handle_init()
        res = base_request.BaseRquest()
        hd_json = handle_json.Handel_json()
        for i in range(2,test_case.get_rows()):
            print ('*'*80,"第",i-1,"个case",'*'*80)
            cookie=None
            data=None
            header=None
            #1、判断是否执行此条case
            if test_case.get_cell_data(i,3)!='yes':
                continue
            #print(test_case.get_cell_data(i,3)) #是否需要执行此case

            #2、读取接口、域名和路径进行拼接（ini文件的host+Excel文件的接口路径）
            if test_case.get_cell_data(i,7)!=None:
                url=hd_ini.read_ini('host','test1')+test_case.get_cell_data(i,7)
                # print("------------------------------------------第", i - 1,"个url---------------------------------------------")
                # print(url)
                # print('url',type(url))
            # 读取依赖case，有值即为有依赖的用例(依赖case)
            if test_case.get_cell_data(i,4)!=None:
                relation_case_line=int(test_case.get_cell_data(i,4))          #获取列表中的关联case行号（获取数据为str，转换为int）
                relation_data=eval(test_case.get_cell_data(relation_case_line,17))  #获取关联列表中的关联数据
            #3、从Excel 表格读取data 信息，data 需要传输str类型
            # print("------------------------------------------第", i - 1,"个data---------------------------------------------")
            if test_case.get_cell_data(i,9)!=None:                            #判断是否需要传参-data
                if test_case.get_cell_data(i,5)!=None: #判断是否需要关联参数，是否是一个关联参数
                    #and len(test_case.get_cell_data(i,5))>1
                    # print("调用函数，传入关联数据、关联参数，获取关联参数对应value")
                    #relation_case_line=int(test_case.get_cell_data(i,4))      #获取关联用例的行数，
                    json_key=test_case.get_cell_data(i,5)                     #获取关联参数的key
                    json_value=hd_json.get_json_values(test_case.get_cell_data(relation_case_line,14),json_key)#获取关联参数的value
                    # print("调用函数，将关联参数-关联参数value填充到读取的data中，返回新的data")
                    data=eval(test_case.get_cell_data(i,9))                   #获取需要传递的data参数
                    data=hd_json.change_json_value(data,json_value)                #将获取的value填充到data参数中
                else:
                    #len(test_case.get_cell_data(i,5))>1:                   #判断是否有多几个关联参数
                    #print("调用多个参数传值函数")
                    data=test_case.get_cell_data(i,9)
                # print('---Excel读取数据data',type(data))
                # print(data)
                # print('---Excel读取转换后数据data',type(data))
            #4、从Excel 表格读取header 信息，header需要字典类型
            # print("------------------------------------------第", i - 1,"个header---------------------------------------------")
            if test_case.get_cell_data(i,11)!=None:         #判断是否需要传递headers
                if test_case.get_cell_data(i,6)!=None:      #判断是否有关联的headers参数
                    #relation_case_line=int(test_case.get_cell_data(i,4))#获取关联header的行数
                    #relation_data=eval(test_case.get_cell_data(relation_case_line,15)) #获取关联行的结果，需要是字典数据类型
                    relation_key= test_case.get_cell_data(i,6)             #获取关联header的参数KEY
                    header = test_case.get_cell_data(i, 11)          #获取header数据
                    # print(header,"-------------old")
                    relation_value=hd_json.get_json_value(relation_data,relation_key)
                    header=eval(header)
                    header=hd_json.change_json_value(header,relation_key,relation_value)
                    # print(header,"---------------new")
                    # print(type(header))
                else:
                    header=test_case.get_cell_data(i,11)
                    header=eval(header)
                # print("header",type(header))
            if test_case.get_cell_data(i,8)!=None:    #判断请求方式是否为空
                #获取需要关联的参数名（i,7），从关联的用例结果中读取对应的值((i,4),14)
                send_f=test_case.get_cell_data(i,8)
                if send_f=="post":
                    # print("url是：",url)
                    # print('data数据类型：',type(data),data)
                    # print('header数据类型：',type(header),header)
                    print("这个是post请求")
                    re=res.send_post(url=url,data=data,cookie=cookie,header=header)
                    print('添加断言')
                    #1、判断状态码---200
                    if re.status_code ==200:
                        test_case.excel_write_data(i,15,re.status_code)
                        test_case.excel_write_data(i,16,eval(re.text)['status'])
                    #2、判断响应的状态----status
                    # print(re.text,type(re.text))
                    #print(re.text)
                    case_result=re.text
                    if test_case.get_cell_data(i,12)!=None:
                        test_case.excel_write_data(i,17,case_result)
                elif send_f=='get':
                    # print("url是：",url)
                    # print('data数据类型：', type(data),data)
                    # print('header数据类型：', type(header), header)
                    data=eval(data)
                    print("这个是get请求")
                    re=res.send_get(url=url, data=data, cookies=cookie, headers=header)
                    # print('添加断言')
                    #1、判断状态码---200
                    # 2、判断响应的状态----status
                    if re.status_code ==200:
                        test_case.excel_write_data(i,15,re.status_code)
                        # print(type(re.text))
                        #test_case.excel_write_data(i,16,eval(re.text)['status'])
                    case_result=re.text
                    if test_case.get_cell_data(i,12)!=None:
                        test_case.excel_write_data(i,17,case_result)
                    # print(re.text,type(re.text))



def add_case():
    case_path = os.path.join(os.getcwd())
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_run_*.py')
    return discover

if __name__ == '__main__':
    # suite=unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(Run_Unit('testcase01'))
    # print(suite)
    # with open(os.path.join(os.path.dirname(os.getcwd()),"report\\test_case.html"),'wb') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="接口测试报告", description="this is test")
    #     runner.run(add_case())
    # f.close()
    hd_ex = handle_excel.Handle_Excel()
    data = hd_ex.get_row_values()
    print(type(data))