# # #创建简单类
# # class Dog():
# #     """"""
# #     def __init__(self,name,age):#创建对象时会自动运行
# #         """
# #         初始化name和age
# #         :param name:
# #         :param age:
# #         """
# #         self.name=name
# #         self.age=age
# #     def sit(self):
# #         """
# #         模拟小狗蹲下
# #         :return:
# #         """
# #         print(self.name.title()+" is now sitting.")
# #     def roll_over(self):
# #         """
# #         模拟小狗打滚
# #         :return:
# #         """
# #         print(self.name.title()+" rolled over!")
# #
# # my_dog=Dog('wellie',6)
# # print("My dog'name is "+my_dog.name.title()+".")
# # print("My dog is "+str(my_dog.age)+" years old")
# # my_dog.sit()
# # my_dog.roll_over()
# # #注释结束
#
# #属性赋值
# class Car():
#     def __init__(self,make,model,year):
#         """
#         初始化汽车的属性
#         :param make:
#         :param model:
#         :param year:
#         """
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odmeter_reading=0#里程数 设置默认值
#     def get_descriptive_name(self):
#         """
#         返回描述信息
#         :return:
#         """
#         long_name=str(self.year)+' '+self.make+' '+self.model
#         return  long_name.title()
#     def read_odmeter(self):
#         """打印汽车里程"""
#         print("This car is "+str(self.odmeter_reading)+"miles on it.")
#     def update_odmeter(self,mileage):
#         """设置里程数"""
#         if mileage>=self.odmeter_reading:#里程数不可回调
#             self.odmeter_reading=mileage
#         else:
#             print("You can't roll back an admeter!")
#     def increment_odmeter(self,miles):
#         """增加指定里程数"""
#         self.odmeter_reading+=miles
# # my_used_car=Car('subaru','outback',2013)
# # print(my_used_car.get_descriptive_name())
# #
# # my_used_car.odmeter_reading=23#直接赋值
# # my_used_car.read_odmeter()
# #
# # my_used_car.update_odmeter(20)#赋值失败
# # my_used_car.read_odmeter()
# #
# # my_used_car.update_odmeter(23500)#方法赋值
# # my_used_car.read_odmeter()
# #
# # my_used_car.increment_odmeter(100)#方法增值
# class Electric_Car(Car):
#     """描述电动汽车"""
#     def __init__(self,make,model,year):
#         """初始化父类"""
#         super().__init__(make,model,year)
#         self.battery=Battery()#实例作属性
#     # def describe_battery(self):
#     #     """打印电瓶容量"""
#     #     print("This car has a "+str(self.battery_size)+"-kwh battery.")
#
# #将实例用作属性
# class Battery():
#     """模拟电动车电瓶"""
#     def __init__(self,battery_size=70):
#         """初始化电瓶属性"""
#         self.battery_size=battery_size
#     def describe_battery(self):
#         """打印电瓶容量"""
#         print("This car has a "+str(self.battery_size)+"-kwh battery.")
#     def get_range(self):
#         """打印消息，指出电瓶续航里程"""
#         if self.battery_size==70:
#             range=240
#         elif self.battery_size==85:
#             range=270
#
#         print("This car can go approximately "+str(range)+" miles on a full charge.")
#
# # my_tesla=Electric_Car('telsa','model s',2016)
# # print(my_tesla.get_descriptive_name())
# # # my_tesla.describe_battery()
# # my_tesla.battery.describe_battery()
# # my_tesla.battery.get_range()
# #注释结束
