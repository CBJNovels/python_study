# #创建字典
# bird={'color':'white and black','food':'hazelnut'}
# print(bird)
# bird['x_position']=0
# bird['y_position']=25
# print(bird)
# #删除字典
# del bird['x_position']
# del bird['y_position']
# print(bird)
# #遍历字典 字典是无序的
# for key,value in bird.items():
#     print('Key:'+key)
#     print('Value:'+value)
# #输出键
# for property in bird.keys():
#     print(property.title())
# for property in bird:#默认遍历键
#     print(property.title())
#
# #排序遍历键
# bird={'food':'hazelnut','color':'white and black','y_position':0,'x_position':0}
# for property in sorted(bird.keys()):
#     print(property.title())
#
# #遍历字典值
# for value in bird.values():
#     print(value)
# #剔除重复值
# for value in set(bird.values()):
#     print(value,end=' ')
# 注释结束

#嵌套
# bird={
#     'pecker':{'scientific name':'woodpecker',
#             'Latin name':'Picidae'},
#     'paradise':{'scientific name':'bird of paradise',
#                 'Latin name':'Paradisaeidae'}
# }
# for b,name in bird.items():
#     print("\nbird:"+b)
#
#     print('\tscientific name:',name['scientific name'],
#           '\n\tLatin name:',name['Latin name'])