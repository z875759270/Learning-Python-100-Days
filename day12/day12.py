
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