# filename='pi_million_digits.txt'
#
# # with open(filename,'w') as file_object:#写入模式下如果文件不存在会自动创建
# #     file_object.write()#如果存在则会清空文件内容！
#
# #处理百万位大型文件
# with open(filename,'r+') as file_object:# 'r+'可读写模式
#     # contents=file_object.read()#整文件读取
#     lines=file_object.readlines()#创建列表获取文件内容 #逐行读取#contents优先获取，lines无法获取
# pi_string=''#创建空的字符串
# for line in lines:
#     pi_string+=line.strip()
# # print(contents)#整文件读取
# print(pi_string[:52]+"...")
# print(len(pi_string))#包括整数位和小数点位
#
# #圆周率中有你的生日吗？
# birthday=input("Enter your birthday,in the form mmddyy: ")
# if birthday in pi_string:
#     print("You birthday appears in the first milion digits of pil!")
# else:
#     print("You birthday does not appear in the first milion digits of pil!")
# #注释结束

# #多行写入
# filename='pi_digits.txt'
# with open(filename,'w') as file_object:#只写模式—覆盖原文件
#     file_object.write("I love programing.")
#     file_object.write("\nI love creating new games.")
# #注释结束
#
# #附加模式 从文件末位写入
# with open(filename,'a') as file_object:#附加模式
#     file_object.write("\nI also love finding meaning in large database.")
#     file_object.write("\nI love creating apps that can run  in a browser.")
# #注释结束