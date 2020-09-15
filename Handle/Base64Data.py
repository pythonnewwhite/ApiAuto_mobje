#导包
import base64

"""使用base64编码进行数据编码转换"""
#原始数据
user_str=b"15900842165"
pw_str=b"12345678c"

#转换为二进制
# user_two=user_str.encode("utf-8")
# pw_two=pw_str.encode("utf-8")
print("user:%s"%user_str)
print("passord: %s"%pw_str)
#使用base64 进行数据转换
user_str_base=base64.b64encode(user_str)
pw_str_base=base64.b64encode(pw_str)
print(user_str_base)
print(pw_str_base)

user=base64.b64decode(user_str_base)
print(type(user))
user=int(user)
print(type(user),user)