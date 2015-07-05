#age.py
name = input("请输入您的名字:")
print("欢迎!", name.capitalize())
age = input("您今年多少岁?")
age50 = int(age) + 50 #int是将age转化为整数
print("50年后您将会是 " + str(age50) + "岁")#str就是将括号内的内容转化为字符串.
#如果不转化为字符串,前面的字符串与数字将无法相加.
if(age50 >= 100):
	print("我不知道你100年后还是否存在")
else:
	print("请珍惜生命")