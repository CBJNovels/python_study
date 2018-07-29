# list=['a','b','c']
# #增加及插入
# list.append('d')
# list.insert(4,'e')
# print(list)
#
# #删除及弹出
# del list[4]
# print(list)
# try:
#     print(list[4])
# except:
#     print('不存在list[4]')
# #注意修改值要记得存入
# print(list.pop())
# print(list)
# list.pop(2)
# print(list)
# #移出相应值
# try:
#     list.remove('b')
#     print(list)
# except:
#     print('列表只剩一个元素时，则变为元素对应类型的变量')

#组织列表
# list=['b','c','a','d']
# print(list)
# #临时排序
# print(sorted(list),end='')
# print(sorted(list,reverse=True),end='')#逆序输出
# print(list)
# #排序
# list.sort()
# print(list,end='')
# list.sort(reverse=True)
# print(list)
#逆序排列
# list.reverse()
# print(list)
#确定列表长度
# print(len(list))
#输出最后一个元素
# print(list)
# print(list[len(list)-1])
# print(list[-1])

#操作列表
#遍历列表
# list=['a','b','c','d']
# for l in list:
#     print(l,end=' ')
#列表元素操作
#Example
# squares=[]
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
# #实验
# list=['please','remember','me']
# for l in list:
#     print(l.title(),end=' ')
#列表统计计算
# list=[1,2,3,4,5,6,7,8,9,0]
# print(list)
# print(min(list))
# print(max(list))
# print(sum(list))

#列表解析
#输出1到10的平方
# squares=[value**2 for value in range(1,11)]
# print(squares)
#输出1到10的立方
# squares=[value**3 for value in range(1,11)]
# print(squares)
#百万输出
# squares=[value for value in range(0,1000001)]
# for i in range(0,1000000):
#         print(squares[i])
#输出奇数
# squares=[value for value in range(1,21,2)]
# for i in range(0,len(squares)):
#     print(squares[i],end=' ')
#输出3的倍数 Unfinshed
# squares=[value%3==0 for value in range(3,31)]
# for i in range(0,len(squares)):
#     print(squares[i])

#列表切片
# list=['a','b','c','d']
# print(list)
# print(list[:2])
# print(list[1:])
# print(list[1:3])
# print(list[-len(list):])#len(list)值为4
# for l in list[-3:]:
#     print(l.upper(),end=' ')

#复制列表
# list=['1','2','3','4','5']
# l=list[:]#切片复制
# l_relevance=list#直接关联
# list.append('Can you look it?')
# print(list)
# print(l)
# print(l_relevance)#直接关联，操作相互，猜测是地址关联

#元组（元组元素不可修改）
# tuple=('1','2','3','4','5')
# print(tuple)
# try:
#     tuple[0]=2
# except:
#     print('修改元组第一个元素，修改失败，元组元素不可更改')
# tuple=('a','b','c','d','e')
# print(tuple)
# print('元组变量可更改')
