#my.py
name = input("What your name?")
name = 'Old user' if name == 'MJK' else 'New user'
print(name)
#等价于:
#if(food == 'lamb'):
#	reply = 'yuck'
#else:
#	reply = 'yum'