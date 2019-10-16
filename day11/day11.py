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
