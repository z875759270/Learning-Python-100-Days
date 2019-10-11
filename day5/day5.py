import random

# %%
""" test1 找出100~1000的所有水仙花数
for x in range(100, 1000):
    a = x//100
    b = x//10 % 10
    c = x % 10
    if (a**3+b**3+c**3)==x:
        print('%d' % (x),end=" ")
"""

""" test2 百钱百鸡
for x in range(0, 20):
    for y in range(0, 33):
        z = 100-x-y
        if (x*5+y*3+z/3) == 100:
            print('公鸡：%d 母鸡：%d 小鸡：%d' % (x, y, z))
"""


# %%
""" test3 Craps赌博游戏
money = 1000

while True:
    print('你当前的资产:%d' % money)
    debt=int(input('请下注：'))
    n = random.randint(1, 6)+random.randint(1, 6)
    print('第一次的点数为:%d' % (n))
    if n == 7 or n == 11:
        print('玩家胜')
        money += debt
    elif n == 2 or n == 3 or n == 12:
        print('庄家胜')
        money -= debt
    else:
        while True:
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            sum = a+b
            print('点数为:%d' % (sum))
            if sum == n:
                print('玩家胜')
                money += debt
                break
            elif sum == 7:
                print('庄家胜')
                money -= debt
                break
    print(money)
    if money <= 0:
        print('憨憨 你的钱莫得辽')
        break
"""

#%%
""" test4 生成斐波那契数列的前n个数。
length=int(input('输入要生成的斐波那契数列的长度：'))
arr=[1,1]
if length>2:
    for i in range(2,length):
        arr.append(arr[i-1]+arr[i-2])
for x in range(0,length):
    print(arr[x],end=" ")
"""

#%%
""" test5 找出10000以内的完美数
arr=[]
for i in range(2,10000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        arr.append(i)
for x in range(0,len(arr)):
    print(arr[x],end=' ')
"""

#%%

""" test6 输出100以内所有的素数。
import math
arr=[]
for i in range(2,100):
    count=0
    for j in range(1,100):
        if i%j==0:
            count+=1
    if count==2:
        arr.append(i)
for x in range(0,len(arr)):
    print(arr[x],end=' ')
"""