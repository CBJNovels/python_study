# #函数默认值
# def describe_pet(pet_name,animal_type='dog'):#已赋值默认值的形参必须在右边
#     """显示宠物的信息"""
#     print("\nI have a "+animal_type+".")
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
#
# describe_pet(pet_name='willie')
#
# #等效函数调用
# #一条名为willie的小狗
# describe_pet('willie')#位置实参及默认值
# describe_pet(pet_name='willie')#关键字实参及默认值
#
# #一只名为Harry的仓鼠
# describe_pet('harry','hamster')#位置实参
# describe_pet(pet_name='harry',animal_type='hamster')#位置实参及关键字实参
# describe_pet(animal_type='hamster',pet_name='harry')#关键字实参
# #注释结束
#
# #函数与while循环结合使用
# def get_formatted_name(first_name,last_name):
#     """返回整洁的名字"""
#     full_name=first_name+' '+last_name
#     return full_name.title()#返回值
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")#退出提示
#
#     f_name=input("First name:")
#     if f_name=='q':#设置退出
#         break
#     l_name=input("Last name:")
#     if l_name=='q':#设置退出
#         break
#     formatted_name=get_formatted_name(f_name,l_name)#获取格式化的名字
#     print("\nHello, "+formatted_name+"!")
# #注释结束
#
# #函数与列表
# def print_models(unprinted_designs,completed_models):
#     """
#     模拟打印，直至unprinted_designs没有元素
#     将unprinted_designs的元素转移到completed_models里
#     :param unprinted_designs:
#     :param completed_models:
#     :return:
#     """
#     while unprinted_designs:
#         current_design=unprinted_designs.pop()
#
#         #模拟3D打印过程
#         print("Printing model:"+current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """
#     显示打印好的所有元素
#     :param completed_models:
#     :return:
#     """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
# unprinted_designs=['iphone case','robot pendant(吊坠)','dodecahedron(十二面体)']
# completed_models=[]
#
# print_models(unprinted_designs[:],completed_models)#备份列表，禁止修改原件且unprinted_designs[:]为副本
# show_completed_models(completed_models)
# #展示原件
# print("\n展示原件")
# for unprinted_design in unprinted_designs:
#     print(unprinted_design)
# #注释结束
#
#传递任意数量的实参（结合位置实参）
def make_pizza(size,*toppings):# size是位置形参：*toppings是一个元组
    """
    打印顾客点的所有配料
    :param size:
    :param toppings:
    :return:
    """
#    打印顾客点的所有配料
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)

# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')
# #注释结束
#
# #使用任意数量的关键字实参
# def bulid_profile(first,last,**user_info):
#     """
#     创建字典user_info，包含用户的信息
#     :param first:
#     :param last:
#     :param user_info:
#     :return:
#     """
#     profile={}
#     profile['first_name']=first
#     profile['last_name']=last
#     for key,value in user_info.items():#字典的特征
#         profile[key]=value
#     return profile
# user_profile=bulid_profile('albert','einstein',
#                            location='princeton',
#                            field='physics')
# print(user_profile)
# #注释结束
