import random
import math
# %%
""" 求1~100和
sum=0
for x in range(101):
    sum+=x
print(sum)
"""

# %%
""" 求1~100偶数和
sum=0
for x in range(2,101,2):
    sum+=x
print(sum)
"""

# %%
""" 猜数字
answer = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = int(input('猜呗:'))
    if num > answer:
        print('大了一些')
    elif num == answer:
        print('猜对了')
        break
    else:
        print('小了一些')
print('你一共猜了%d次' % (count))
if count > 6:
    print('属实铁憨憨嗷')
"""

# %%
""" 输出九九乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print('%d * %d = %d' % (i, j, i*j),end='\t')
"""

# %%
""" test1 输入一个整数判断它是不是质数
x = int(input())
num = int(math.sqrt(x))
isP = True
for i in range(2, num+1):
    if x % i == 0:
        isP = False
        break
if isP and x != 1:
    print('是质数')
else:
    print('不是质数')
"""

# %%
""" test2 输入两个正整数，计算它们的最大公约数和最小公倍数。
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
"""

#%%
""" test3 输出星星
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
"""
    

    