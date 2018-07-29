# #异常
# try:
#     print(5/0)
# except:
#     print("You can't divide by zero!")
#
# #处理ZeroDivisionError异常
# print("Give me two numbers,and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number=input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number=input("Second_number: ")
#     try:
#         answer=int(first_number)/int(second_number)
#     except ZeroDivisionError:#ZeroDivisionError异常对象
#         print("You can't divide by zero!")
#     else:
#         print(answer)#输出结果
# #注释结束

# #处理FileNotFoundError异常
# # filename='alice.txt'
# # try:
# #     with open(filename) as f_obj:
# #         contents=f_obj.read()
# # except:
# #     msg="Sorry,the file "+filename+" does not exist."
# #     print(msg)
# # #注释结束

# #分析文本方法
# # filename='alice.txt'
# filenames=['alice.txt','siddhartha.txt']
#
# def count_words(filename):
#     """计算文本单词数"""
#     try:
#         with open(filename) as f_obj:
#             contents=f_obj.read()
#     except FileNotFoundError:
#         # pass#略过
#         msg="Sorry,the file "+filename+" does not exist."
#         print(msg)
#     else:
#         words=contents.split()#以空格为分隔符拆分字符串为列表
#         num_words=len(words)
#         print("The file "+filename+" has about "+str(num_words)+" words.")
#
# for filename in filenames:
#     count_words(filename)
# #注释结束