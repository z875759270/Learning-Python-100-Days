import math
""" 获取类型
a=100
b=1+5j
c=1.23
d='slak'
e=False

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""

""" 占位符
a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a+b))
print('%d - %d = %d' % (a, b, a-b))
print('%d * %d = %d' % (a, b, a*b))
print('%d / %d = %d' % (a, b, a/b))
print('%d // %d = %d' % (a, b, a//b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a**b))
"""

""" 逻辑运算符
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False
"""

""" test1 华氏温度转换为摄氏温度
f=int(input('℉ = '))
print('℉ = %.1f \n℃ = %.1f' % (f,(f-32)*5/9))
"""

""" test2 输入圆的半径计算计算周长和面积
r = float(input('r = '))
print('r=%.2f \n long=%.2f \n area=%.2f' % (r, 2*math.pi*r, math.pi*(r**2)))
"""

""" test3 判断闰年
year = int(input('year = '))
# 如果代码太长写成一行不便于阅读 可以使用\\对代码进行折行
isRun = (year % 4 == 0 and year % 100 != 0) or \
        year % 400 == 0
print(isRun)
"""
