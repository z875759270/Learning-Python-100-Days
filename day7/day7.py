import time
import os
import sys
# %%
"""
# 使用'*'来对字符串进行重复
s1 = 'hello ' * 3
print(s1)  # hello hello hello

# 使用关键字'in'来判断字符串内是否包括另一字符串
print('ll' in s1)  # True

# 从字符串中取出指定位置的字符
s2 = 'abcdef'
print(s2[4])  # e

# 截取字符
s3 = 'niupiao'
print(s3[2:5])  # upia
print(s3[2:])  # upiao
print(s3[2::2])  # uio
print(s3[::2])  # nuio
print(s3[::-1])  # oaipuin
print(s3[-3:-1])  # ia

a, b = 10, 4
print(f'{a} * {b}={a * b}')
"""

# %%
"""
# 使用列表的生成式语法来创建列表
f=[i for i in range(1,10)]
print(f)
f=[x+y for x in 'ABCDE' for y in '1234567']
print(f)

# 使用生成表达式语法创建列表（耗费更多的内存空间）
f=[x ** 2 for x in range(1,100)]
print(sys.getsizeof(f))
print(f)

# 下面的代码创建的不是列表而是生成器（耗费更多的时间）
f=(x ** 2 for x in range(1,100))
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val,end=',')
"""

# %%
""" 元组
#定义元组
t = ('zzzz',12,True,'牛批')

#将元组转换成列表
p=list(t)

#将列表转换成元组
t=tuple(p)
"""

# %%
""" 字典 
#字典的定义
cha={'一号':95,'二号':78,'三号':82}
print(cha['一号'])

#遍历字典
for x in cha:
    print('%s\t--->\t%d' % (x,cha[x]))

#更新字典中的元素
cha['一号']=77 
cha['四号']=22
print(cha)

#删除字典中的元素
print(cha.popitem()) # 默认删除末尾
print(cha.popitem())
print(cha.pop('四号',22))
print(cha)
"""

# %%
""" test1 跑马灯文字
def main():
    content = "辣是真滴牛批..."
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]


if __name__ == "__main__":
    main()
"""

# %%
""" test2 生成指定长度的验证码 
import random

def CreatCode():
        length=int(input('指定长度：'))
        text="ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwxyz0123456789"
        res=''
        for _ in range(1,length+1):
            res+=text[random.randint(0,len(text))] 
        print(res)
"""

# %%
""" test3 设计一个函数返回给定文件名的后缀名
def GetEndWith(filename):
    if '.' in filename:
        return filename[filename.find('.'):]
    else:
        return print('文件名中不含.')

print(GetEndWith('1.txt'))
"""

# %%
""" test4 返回传入的列表中最大和第二大的元素的值 
def MaxAndSecond(x):
    temp=list(x)
    l=sorted(temp,reverse=True)
    return l[0],l[1]

l=[4,7,8,24,1,65,84,7,10,6]
print(MaxAndSecond(l))
"""

# %%
""" test5 计算指定的年月日是这一年的第几天
def main():
    def a(year,month,day):
        count=0
        if year%100!=0 and year%4==0 or year%400==0:
            arr=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            arr=[31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(0,month-1):
                count+=arr[i]
        count+=day
        return count
    print(a(2008,3,1))

if __name__ == "__main__":
    main()
"""

# %%
""" test6 打印杨辉三角
def main():
    def ss(n):
        arr1=[1,1]
        arr2=[1]
        print(arr2)
        for _ in range(1,n):
            print(arr1)
            arr2=[1]
            for x in range(1,n+1):
                try:
                    arr2.append(arr1[x-1]+arr1[x])
                except:
                    continue
            arr2.append(1)
            arr1=arr2
            
                
    ss(int(input('请输入要生成的杨辉三角的行数：')))
    
if __name__ == "__main__":
    main()
"""

# %%
""" demo2 """
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，
报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人
。由于上帝的保佑，15个基督徒都幸免于难，
问这些人最开始是怎么站的，
哪些位置是基督徒哪些位置是非基督徒。
"""
"""
def main():
    arr=[]
    for _ in range(0,30):
        arr.append(True)
    index,num,count=0,0,0
    while count<15:
        num+=1
        if num==9:
            arr[index]=False
            num=0
            count+=1
        index+=1
        index%=30

    for i in arr:
        print('基' if i else '非', end=" ")
    
if __name__ == "__main__":
    main()
"""

# %%
""" demo3 井字棋游戏 
#加载/刷新棋盘
def loadchess(chess):
    print(chess[0][0] + '|' + chess[0][1] + '|' + chess[0][2])
    print('-+-+-')
    print(chess[1][0] + '|' + chess[1][1] + '|' + chess[1][2])
    print('-+-+-')
    print(chess[2][0] + '|' + chess[2][1] + '|' + chess[2][2])

#判断胜负
def whowins(chess):
    for i in range(0,len(chess)):
        for j in range(0,len(chess)):
            try:
                if chess[i][j]==chess[i+1][j]==chess[i+2][j]:
                    return chess[i][j]
            except:
                pass
            try:
                if chess[i][j]==chess[i][j+1]==chess[i][j+2]:
                    return chess[i][j]
            except:
                pass
            try:
                if chess[i][j]==chess[i+1][j+1]==chess[i+2][j+2]:
                    return chess[i][j]
            except:
                pass
            try:
                if chess[i][j]==chess[i-1][j-1]==chess[i-2][j-1]:
                    return chess[i][j]
            except:
                pass

def main():
    chess = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    count = 0
    people = 'x'
    while count < 9:
        s = input('轮到%s,请输入下棋的位置:' % people)
        temp = s.split(',')
        if chess[int(temp[0])][int(temp[1])]==' ':
            chess[int(temp[0])][int(temp[1])]=people
        else:
            print("该位置已有棋子，请重新输入")
            continue
        if people == 'x':
            people = 'o'
        else:
            people = 'x'
        count += 1
        loadchess(chess)
        res=whowins(chess)
        if res!= ' ':
            print("%s取得了胜利！" % res)
            break

if __name__ == '__main__':
    main()
"""
arr=[[11,11]]*3
print(arr)