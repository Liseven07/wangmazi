
# #print方法
# print("你好 全世界！")      #字符串
# print(1777)               #数字 
# print(1.2222)           #小数
# print(False)        #布尔值 ： True 和 False
# print(())           #元组
# print([])           #数组
# print({})           #字典


# # 锄禾日当午
# # 汗滴禾下土

# print("你笑着说","他是朋友",886) #逗号隔开表现为空格
# print("哈哈"+"嘻嘻")        #字符串的拼接
# print("哈"*7)
# print(((1+1)*2-1)/3)
# print(1>2)


# #input方法
# a="王麻子"
# print(a)
# a=input("请输入：")   #input 获取的是字符型数据
# b=input("请输入：")
# print("input获取的内容：",a+b)

# #type方法
# print(type("你好"))
# print(type(222))
# print(type(2.22))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))
# a=100+9
# print(int(a))
# x=float(input("请输入："))
# y=float(input("请输入："))
# print("input获取的内容：",x+y)

#len方法  只支持字符串、元组、数组、字典的长度获取
str1=input("请输入第一段话：")
str2=input("请输入第二段话：")
a=str1+"，"+str2
print("通知：",a)
print("两段话的总长度：",len(str1)+len(str2),len(a))

#str方法

#int方法