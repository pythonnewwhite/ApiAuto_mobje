# coding=utf-8
import os
import sys
import json
import handle_excel
"""
json 操作的四大方法；dump 、dumps、load、loads
    读取json 数据
    load方法、从文件中读取json 文件
    loads 读取str类型的json 数据
1、文件读取json---json.load（file_path,encoding="utf-8"）
    str 类型转换 dict  ---json.loads(str_data)
2、json 取值---load、loads 读取的json文件类型是 dictionary（字典）可以通过key值取 value 值
     
3、


with open(base_path, encoding="utf-8") as f:
#ff=open(base_path)
    data=json.load(f)
    data_value=data.get("data")
    token=data_value.get("token")
    print (token)
    print (data_value)
    print (type(data_value))
    print (data.get("status"))
    print(type(data.get("status")))

"""

class Handel_json:
    base_path=os.path.join(os.path.dirname(os.getcwd()))
    def read_json(self,file_name=None):
        if file_name==None:
            file_path=os.path.join(self.base_path+"\\config\\package.json")
        else:
            file_path=os.path.join(self.base_path + file_name)
        with open(self.base_path,encoding="utf-8") as f:
            data=json.load(f)
        return data
    def get_token(self,file_name=None):
        data=self.read_json(file_name)
        return data.get("data").get("token")

    def get_value(self,file_name=None):
        data=self.read_json(file_name)
        return data.get("status")

    def write_value(self,data_send,file_name=None):
        data=json.dumps(data_send)
        if file_name== None:
            file_path=os.path.join(self.base_path+"\\config\\package.json")
        else:
            file_path=self.base_path+file_name
        with open(file_path,"w") as f:
            f.write(data)
    def read_str_json(self,data_str):
        res=json.loads(data_str)
        print (res)
        return res

    def get_json_value(self,json_data,json_key):
        """根据 传入的json_key 获取json中对应的value，以str的数据类型返回"""
        if isinstance(json_data,dict):
            for i in json_data.keys():
                if json_key in json_data.keys():  # 判断 是否是输入的 KEY，返回value
                    json_value=json_data[json_key]
                    return json_value
                if isinstance(json_data[i],dict):
                        return self.get_json_value(json_data[i],json_key)
                if isinstance(json_data[i],list): #判断 参数是否是list类型，是就遍历list列表参数，有字典就递归，无就对比KEY
                        for j in (json_data[i]):
                            if isinstance(j,dict):
                               return self.get_json_value(j,json_key)


    def get_json_values(self,json_data,json_key,json_value_list=[]):
        """根据 传入的json_key 获取json中对应的value，以列表的格式返回"""
        for i in json_data.keys():
            if i is json_key:
                json_value=json_data[i]
                json_value_list.append(json_value)
            elif isinstance(json_data[i],dict):
                 self.get_json_values(json_data[i],json_key,json_value_list)
            elif isinstance(json_data[i],list):
                for j in range(len(json_data[i])):
                    if isinstance(json_data[i][j],dict):
                        self.get_json_values(json_data[i][j],json_key,json_value_list)
        return json_value_list

    def change_json_value(self, json_data, json_key, json_value):
        '''
        传参json_data 和返回值为字典格式
        '''
        if isinstance(json_data, dict):
            if json_key in json_data.keys():
                json_data[json_key] = json_value
                return json_data
            else:
                print(json_key, "不存在")
        else:
            print(json_data, "不是字典格式")
if __name__ == '__main__':
    data = {"status": "SUCCESS", "data": {"user": {"id": 161, "aid": "3002720200722171100017"}}}
    print(data["status"])
    status=data["status"]
    print(status == "SUCCESS")
    '''h_j=Handel_json()
    data='{"status": "SUCCESS", "data": {"user": {"id": 161, "aid": "3002720200722171100017"}}}'
    #data={"status": "SUCCESS", "data": {"user": {"id": 161, "aid": "3002720200722171100017"}}}
    #data='{"errno":0,"errmsg":null,"unassigned":0,"total":0,"list":null}'
    res=h_j.read_str_json(data)
    print(res.get("data").get("user"))
    print (type(res))
    #h_j.write_value(data_send=data,file_name=None)

    data ={"status": "SUCCESS", "data": {"user": {"id": 161, "aid": "3002720200722171100017"}}}
    print(type(data))
    data=json.loads(data)
    print(type(data))

    '''
    # hd_excel=handle_excel.Handle_Excel()
    # hd=Handel_json()
    # json_data=hd_excel.get_cell_data(2,15,index=0)
    # json_key=hd_excel.get_cell_data(3,6,index=0)
    # print(json_key)
    # json_data=eval(json_data)
    # print(json_data)

    #json_data ={"status":"SUCCESS",'aid':["tt",121],"data":{"user":[{"a":"b","aid":'302',"name":"小学生"}]}}
    # json_data={'status': 'SUCCESS','permals': [1, 2],'data': {'user': {'id': 174, 'workrCount': 0,'cardNo':'41185317'},'token':'4OAbCoYM6_w6Ekk8NyXU-85M3KuEDzsKcVuEyqGw'}}
    # print(Handel_json().get_json_value(json_data,json_key))
