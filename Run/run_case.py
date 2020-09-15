# coding=utf-8
import os
import sys
import configparser
import json
import requests
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\Run')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\Handle')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\Base')
sys.path.append('C:\\soft\\Pycharm\\PyCharm 2019.1.3\\helpers\\pycharm_display')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\venv\\Scripts\\python37.zip')
sys.path.append('C:\\Users\\TimaNetworks\\AppData\\Local\\Programs\\Python\\Python37\\DLLs')
sys.path.append('C:\\Users\\TimaNetworks\\AppData\\Local\\Programs\\Python\\Python37\\lib')
sys.path.append('C:\\Users\\TimaNetworks\\AppData\\Local\\Programs\\Python\\Python37')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\venv')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\venv\\lib\\site-packages')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.7.egg')
sys.path.append('C:\\soft\\Pycharm\\workspace\\new_mojie\\venv\\lib\\site-packages\\pip-19.0.3-py3.7.egg')
sys.path.append('C:\\soft\\Pycharm\\PyCharm 2019.1.3\\helpers\\pycharm_matplotlib_backend')
from Handle import handle_json
from Handle import handle_init
from Handle import handle_excel
from Base import base_request

if __name__ == '__main__':
    test_case=handle_excel.Handle_Excel()
    sheet_name=test_case.get_sheet_data(0)
    hd_ini=handle_init.Handle_init()
    res=base_request.BaseRquest()
    hd_json=handle_json.Handel_json()
    # print (type(re))

    for i in range(2,test_case.get_rows()):
        print ("------------------------------------------第",i-1,"个case---------------------------------------------")
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
            print("------------------------------------------第", i - 1,"个url---------------------------------------------")
            print(url)
            # print('url',type(url))
        # 读取依赖case，有值即为有依赖的用例(依赖case)
        if test_case.get_cell_data(i,4)!=None:
            relation_case_line=int(test_case.get_cell_data(i,4))          #获取列表中的关联case行号（获取数据为str，转换为int）
            relation_data=eval(test_case.get_cell_data(relation_case_line,15))  #获取关联列表中的关联数据
        #3、从Excel 表格读取data 信息，data 需要传输str类型
        print("------------------------------------------第", i - 1,"个data---------------------------------------------")
        if test_case.get_cell_data(i,9)!=None:                            #判断是否需要传参-data
            if test_case.get_cell_data(i,5)!=None: #判断是否需要关联参数，是否是一个关联参数
                #and len(test_case.get_cell_data(i,5))>1
                print("调用函数，传入关联数据、关联参数，获取关联参数对应value")
                #relation_case_line=int(test_case.get_cell_data(i,4))      #获取关联用例的行数，
                json_key=test_case.get_cell_data(i,5)                     #获取关联参数的key
                json_value=hd_json.get_json_values(test_case.get_cell_data(relation_case_line,14),json_key)#获取关联参数的value
                print("调用函数，将关联参数-关联参数value填充到读取的data中，返回新的data")
                data=eval(test_case.get_cell_data(i,9))                   #获取需要传递的data参数
                data=hd_json.change_json_value(data,json_value)                #将获取的value填充到data参数中

            else:
                #len(test_case.get_cell_data(i,5))>1:                   #判断是否有多几个关联参数
                #print("调用多个参数传值函数")
                data=test_case.get_cell_data(i,9)
            print('---Excel读取数据data',type(data))
            print(data)
            print('---Excel读取转换后数据data',type(data))
        #4、从Excel 表格读取header 信息，header需要字典类型
        print("------------------------------------------第", i - 1,"个header---------------------------------------------")
        if test_case.get_cell_data(i,11)!=None:         #判断是否需要传递headers
            if test_case.get_cell_data(i,6)!=None:      #判断是否有关联的headers参数
                #relation_case_line=int(test_case.get_cell_data(i,4))#获取关联header的行数
                print(relation_case_line)
                #relation_data=eval(test_case.get_cell_data(relation_case_line,15)) #获取关联行的结果，需要是字典数据类型
                relation_key= test_case.get_cell_data(i,6)             #获取关联header的参数KEY
                header = test_case.get_cell_data(i, 11)          #获取header数据
                print(header,"-------------old")
                relation_value=hd_json.get_json_value(relation_data,relation_key)
                header=eval(header)
                header=hd_json.change_json_value(header,relation_key,relation_value)
                print(header,"---------------new")
                print(type(header))
            else:
                header=test_case.get_cell_data(i,11)
                header=eval(header)
            # print("header",type(header))
        if test_case.get_cell_data(i,8)!=None:    #判断请求方式是否为空
            #获取需要关联的参数名（i,7），从关联的用例结果中读取对应的值((i,4),14)
            send_f=test_case.get_cell_data(i,8)
            if send_f=="post":
                print(type(data))
                print(type(header))
                print("这个是post请求")
                re=res.send_post(url=url,data=data,cookie=cookie,header=header)
                print(re)
                print(re.text)
                case_result=re.text
                if test_case.get_cell_data(i,12)!=None:
                    test_case.excel_write_data(i,15,case_result)
            elif send_f=='get':
                data=eval(data)
                print("这个是get请求")
                re=res.send_get(url=url, data=data, cookies=cookie, headers=header)
                case_result=re.text
                if test_case.get_cell_data(i,12)!=None:
                    test_case.excel_write_data(i,15,case_result)
                print(re)
                print(re.text)
