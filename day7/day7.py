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

#%%
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

#%%
""" test4 返回传入的列表中最大和第二大的元素的值 
def MaxAndSecond(x):
    temp=list(x)
    l=sorted(temp,reverse=True)
    return l[0],l[1]

l=[4,7,8,24,1,65,84,7,10,6]
print(MaxAndSecond(l))
"""

#%%

def main():
    

if __name__ == "__main__":
    main()