# coding=utf-8

# %%
""" if...else的使用
uname = input('用户名:')
upsw = input('密  码:')
if uname=='111' and upsw=='111':
    print('登录成功')
else:
    print('登陆失败')
"""

# %%
"""  if...elif..else的使用
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
"""

# %%
""" test1 英制单位英寸与公制单位厘米的互换
length = float(input('请输入长度：'))
dw = input('请输入单位：')

if dw == 'cm' or dw == '厘米':
    print('%.2fcm = %.2fin' % (length, length/2.54))
elif dw == 'in' or dw == '英寸':
    print('%.2fin = %.2fcm' % (length, length*2.54))
else:
    print('请输入有效的单位')
"""

# %%
""" test2 输入三条边，判断是否能构成三角形并计算周长和面积
a = float(input('第一条边:'))
b = float(input('第二条边:'))
c = float(input('第三条边:'))

if a+b > c and a+c > b and b+c > a:
    p=float((a+b+c)/2)
    print('三角形的周长为:%.2f  三角形的面积为:%.2f'\
         % (a+b+c, (p*(p-a)*(p-b)*(p-c))**0.5))
else:
    print('输入的边长无法构成三角形')
"""