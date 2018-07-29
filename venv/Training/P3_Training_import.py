# #方法导入
# import P3_Training_function as tf#别名
# from P3_Training_function import make_pizza as mp#别名
# from P3_Training_function import *#导入全部函数
# mp(16,'pepperoni')
# mp(12,'mushrooms','green peppers','extra cheese')
#
# #导入类
# from P3_Training_class import Electric_Car,Car
# my_used_car=Car('subaru','outback',2013)
# print(my_used_car.get_descriptive_name())
#
# my_tesla=Electric_Car('telsa','model s',2016)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

#导入有序字典方法
# from collections import OrderedDict
#
# favorite_language=OrderedDict()#创建有序字典
#
# favorite_language['jen']='python'
# favorite_language['sarah']='c'
# favorite_language['edwaid']='ruby'
# favorite_language['phil']='python'
#
# for name,language in favorite_language.items():
#     print(name.title()+"'s favorite language is "+language.title()+'.')