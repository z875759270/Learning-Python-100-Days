# %%
""" 定义一个函数 
def add(a,b):
    return a+b

print(add(1,5))
"""

# %%
""" 重载的另一种实现(指定参数的默认值)
def two(a=1,b=2):
    return a+b

print(two())
print(two(2,3))
"""

# %%
""" 不确定参数个数时可以使用可变参数 （在参数名前面添加 ‘ * ’）
def three(*args):
    sum=0
    for x in args:
        sum+=x
    return sum
print(three())
print(three(1,3,5,8))
"""

# %%
""" 不同模块（模块即文件）可以存在相同名字的函数
# 区分方法1(个人推荐)
import demo1 as d1
import demo2 as d2
d1.ccc()
d2.ccc()

# 区分方法2(顺序很重要)
from demo1 import ccc
ccc()
from demo2 import ccc
ccc()
"""

# %%
""" 导入模块时会执行该模块的代码 当我们不希望如此时可以使用 if __name__ =='__main__': 详见demo3
import demo3
"""

# %%
""" test1 实现计算求最大公约数和最小公倍数的函数
def gcd(x, y):
    # 求最大公约数
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    #求最小公倍数
    return x * y // gcd(x, y)
"""

# %%
""" test2 实现判断一个数是不是回文数的函数 """
def is_hws(a):
    temp=a
    hws=0
    while temp>0:
        hws=hws*10+temp%10
        temp //= 10
    return hws==a

# %%
""" 实现判断一个数是不是素数的函数 """
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

# %%
""" 判断输入的正整数是不是回文素数 """
if __name__=="__main__":
    num=int(input('请输入正整数：'))
    if is_hws(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)