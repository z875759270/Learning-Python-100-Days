#%% 读取文件
"""
def main():
    f=None
    try:
        f=open('Learning-Python-100-Days/day11/day11.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('未找到指定文件！')
    except LookupError:
        print("指定了未知的编码！")
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    main()

"""

""" 逐行打印
import time

def main():
    with open('Learning-Python-100-Days/day11/day11.txt','r',encoding='utf-8') as f:
        print(f.read())

    with open('Learning-Python-100-Days/day11/day11.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            time.sleep(0.5)
    print()

    with open('Learning-Python-100-Days/day11/day11.txt',encoding='utf-8') as f:
        lines=f.readlines()
    print(lines)

if __name__ == "__main__":
    main()
"""

"""  写入文件
def main():
    # 'a'追加写入 'w'覆盖写入
    with open('Learning-Python-100-Days/day11/demo1.txt','a',encoding='utf-8') as f:
        f.write('辣是真滴牛批嗷++')
    print()
    
if __name__ == "__main__":
    main()
"""

""" 读写二进制文件 复制
def main():
    try:
        with open('Learning-Python-100-Days/day11/demo2.jpg','rb') as fs1:
            data=fs1.read()
            print(type(data))
        with open('Learning-Python-100-Days/day11/demo3.jpg','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('')
if __name__ == "__main__":
    main()
"""

""" 保存Json格式文件
import json

def main():
    mydict={
        'name':'牛啊',
        'age':38,
        'qq':77777,
        'friends':['sss','sss'],
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand':'Audi','max_speed':200},
            {'brand':'Benz','max_speed':320}
        ]
    }
    try:
        with open('Learning-Python-100-Days/day11/data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成')
if __name__ == "__main__":
    main()
"""

""" 调用API，读取Json数据
import requests
import json

resp=requests.get('http://api.tianapi.com/txapi/weibohot/?key=b5030c60e54423584d03cb187cd66f52')
data=json.loads(resp.text)
title=[]
hotnum=[]
for t in data['newslist']:
    title.append(t['hotword'])
for n in data['newslist']:
    hotnum.append(n['hotwordnum'])

for x in range(0,len(title)):
    print('热点词：%s  热度:%d' % (title[x],int(hotnum[x])))
"""



""" 正则表达式验证
import re

def main():
    username=input('请输入用户名：')
    qq=input('请输入QQ号：')
    m1=re.match(r'^[0-9A-Za-z_]{6,20}$',username)
    m2=re.match(r'^[1-9]\d{4,11}$',qq)
    if not m1:
        print('请输入有效的用户名.')
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你的输入是有效的')

if __name__ == "__main__":
    main()
"""

"""
import re


def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
"""

""" 替换字符串中的不良内容
    import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()
"""

""" 拆分字符串
import re
def main():
    poem='床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    res=re.split(r'[，。，。]',poem)
    while '' in res:
        # 去除结尾的空白
        res.remove('')
    print(res)

if __name__ == "__main__":
    main()
"""