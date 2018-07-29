#存储数据
import json

# #存储与加载
# numbers=[2,3,5,7,11,13]
# filename='numbers.json'
# with open(filename,'w') as f_obj:
#     json.dump(numbers,f_obj)#存储
# with open(filename) as f_obj:#不能以只读模式加载
#     json.load(f_obj)#加载
#
# print(numbers)

# #保存和读取用户生成数据
# filename='username.json'
# try:
#     with open(filename) as f_obj:
#         username=json.load(f_obj)
# except FileNotFoundError:#首次运行才会执行
#     username = input("What is your name?")
#     with open(filename,'w') as f_obj:
#         json.dump(username,f_obj)
#         print("We will remember you when you come back, "+username+"!")
# else:
#     print("Welcome back,"+username+"!")
# #注释结束

