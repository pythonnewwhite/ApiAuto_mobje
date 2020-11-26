# coding=utf-8
import configparser
import os
import json
from Handle.handle_json import Handel_json
'''
base_path=os.path.dirname(os.getcwd())
file_path=os.path.join(base_path+'\\config\\test.ini')
print (file_path)
'''
class Handle_init:
    file_path = os.path.join(os.path.dirname(os.getcwd()) + '\\config\\test.ini')
    def load_ini(self):
        cf=configparser.ConfigParser()
        cf.read(self.file_path)
        return cf
    def read_ini(self,key,node=None):
        """使用ConfigParser 的 get（section，option）方法进行数据读取，
        key是option参数，node 为section参数 """
        cf=self.load_ini()
        data=cf.get(node,key)
        return data
    def addsection(self):
        """添加section"""
        cf=self.load_ini()
        # cf.add_section("test3")

    def write_ini(self,option,data,section="test1"):
        '''
        option 为key，传值必须为str类型
        data为对应的value;传值必须为str类型
        '''
        cf=self.load_ini()
        # cf.write(open(self.file_path, 'w'))
        cf.set(section=section,option=option,value=data)
        cf.write(open(self.file_path, 'w'))
    def read_token(self,key="token",option="login",node=None):
        """key 为需要获取数据的key，option为对应section的option，node为对应的section"""
        value = json.loads(self.read_ini(option, node=node))
        if value !="":
            value=json.loads(self.read_ini(option,node=node))
        else:
            print ("未从ini文件中读取到",option,"的值")
        token=Handel_json().get_json_value(value,key)
        return token

if __name__ == '__main__':
    tt=Handle_init()
    token=tt.read_token("token","login","test2")
    print("token",type(token),token)
    section='test3'
    option='token1'
    data='[{"1":"1"}]'
    # tt.write_ini(option,data)
    tt.write_ini(section=section,option=option,data=option)
    # tt.write_ini(section=section,option=option,data=data)
    # file_path = os.path.join(os.path.dirname(os.getcwd()) + '\\config\\test.ini')
    # cf = configparser.ConfigParser()
    # cf.read(file_path, encoding='utf-8')
    # section='test1'
    # option='tokenx'
    # data="xxxxx"
    # cf.set(section=section,option=option,value=option)
    # cf.set(section=section,option=option,value=data)
    # cf.write(open(file_path,'w'))
