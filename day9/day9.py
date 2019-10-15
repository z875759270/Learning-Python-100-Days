# %%
""" @property装饰器
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在飞行棋.' % (self._name))
        else:
            print('%s正在斗地主.' % (self._name))

def main():
    p1=Person('牛嗷',12)
    p1.play()
    p1.age=20
    p1.play()
    # p1.name = '憨嗷'  # AttributeError: can't set attribute

if __name__ == "__main__":
    main()
"""

# %%
""" __slots__魔法 
class Person(object):
    __slots__=('_name','_age','_gender')

    def __init__(self,name,age):
        self._name=name
        self._age=age

    def __str__(self):
        return ('%s,%d' % (self._name,self._age))

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age


    @age.setter
    def age(self,age):
        self._age=age
    
    def play(self):
        if self._age <= 16:
            print('%s正在飞行棋.' % (self._name))
        else:
            print('%s正在斗地主.' % (self._name))

def main():
    p1=Person('牛嗷',12)
    print(p1)
    p1.play()
    p1._gender='男'


if __name__ == "__main__":
    main()         
"""

# %%
""" 静态方法
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


if __name__ == '__main__':
    main()
"""

""" 类方法 
from time import time, localtime, sleep


class Clock(object):
    #数字时钟

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        # 走字
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        # 显示时间
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
"""

""" 继承 

class Character(object):

    def __init__(self, name, hp, mp, level):
        self._name = name
        self._hp = hp
        self._mp = mp
        self._level = level

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp

    @property
    def level(self):
        return self._level

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @mp.setter
    def mp(self, mp):
        self._mp = mp

    @level.setter
    def level(self, level):
        self._level = level

    def update_hp(self, num):
        self._hp += num
        print("当前血量为：%d" % self._hp)

    def update_mp(self, num):
        self._mp += num
        print("当前蓝量为：%d" % self._mp)

    def level_up(self):
        self._level += 1
        print("升级啦！当前等级为：%d" % self._level)


class Player(Character):
    def __init__(self, name, hp, mp, level, is_jump=False, is_run=False):
        super().__init__(name, hp, mp, level)
        self._is_jump = is_jump
        self._is_run = is_run

    @property
    def is_jump(self):
        return self._is_jump

    @is_jump.setter
    def is_jump(self, is_jump):
        self._is_jump = is_jump

    @property
    def is_run(self):
        return self._is_run

    @is_run.setter
    def is_run(self, is_run):
        self._is_run = is_run

    def run(self):
        self._is_run = True
        print('跑步中')

    def jump(self):
        self._is_jump = True
        print('蹦起来辽')


class Monster(Character):
    def __init__(self, name, hp, mp, level, is_auto=True):
        super().__init__(name, hp, mp, level)
        self._is_auto = is_auto

    @property
    def is_auto(self):
        return self._is_auto

    @is_auto.setter
    def is_auto(self, is_auto):
        self._is_auto = is_auto

    def stop_auto(self):
        self._is_auto = False
        print('停止自动寻路')


def main():
    player = Player('牛', 100, 100, 1)
    monster = Monster('木偶一号', 10, 99999, 1)
    player.run()
    monster.stop_auto()
    player.level_up()
    monster.update_hp(-15)


if __name__ == "__main__":
    main()

"""

""" 多态 

from abc import ABCMeta, abstractmethod

# 注意引用
class Pet(object, metaclass=ABCMeta):
    # 宠物
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        # 发出声音
        pass

class Dog(Pet):
    # 狗

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    # 猫

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
"""

"""demo1 主角打憨批 """
from random import randint
from abc import abstractmethod,ABCMeta

class Character(object,metaclass=ABCMeta):

    def __init__(self, name, hp, mp, attack):
        self._name = name
        self._hp = hp
        self._mp = mp
        self._attack = attack

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp

    @property
    def attack(self):
        return self._attack

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @mp.setter
    def mp(self, mp):
        self._mp = mp

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    def update_hp(self, num):
        self._hp += num
        print("当前血量为：%d" % self._hp)

    def update_mp(self, num):
        self._mp += num
        print("当前蓝量为：%d" % self._mp)

    @abstractmethod
    def attack_to(self,other):
        pass

class Player(Character):
    def __init__(self, name, hp, mp, attack):
        super().__init__(name, hp, mp, attack)

    def attack_to(self,other):
        other.hp-=randint(15,20)*self.attack

    def magic_attack(self,others):
        if self._mp>=20:
            self._mp-=20
            for other in others:
                other.hp-=randint(10,15)
            return True
        else:
            return False

class Monster(Character):
    def __init__(self, name, hp, mp, attack):
        super().__init__(name, hp, mp, attack)

    def attack_to(self,other):
        other.hp-=randint(5,10)*self.attack

def main():
    p=Player('牛批',300,100,1.7)
    m1=Monster("憨批一号",100,100,1.1)
    m2=Monster("憨批二号",90,100,1.2)
    m3=Monster("憨批三号",80,100,1.3)
    ms=[m1,m2,m3]
    round=1
    while True:
        print('--------------------\n第%d回合：' % (round))
        print('当前玩家状态：\n血量：%d 蓝量：%d' % (p.hp,p.mp))
        print('当前憨批状态：')
        for x in ms:
            print('%s 血量：%d 蓝量：%d' % (x.name,x.hp,x.mp))
        if p.hp>0:
            if randint(1,11)>6:
                if p.magic_attack(ms):
                    print('玩家使用了群体魔法攻击！')
                else:
                    print('玩家蓝量不足！使用普通攻击')
                    while True:
                        temp=ms[randint(0,2)]
                        if temp.hp>0:
                            p.attack_to(temp)
                            break
                
            else:
                print('玩家使用普通攻击')
                while True:
                    temp=ms[randint(0,2)]
                    if temp.hp>0:
                        p.attack_to(temp)
                        break

        for i in ms:
            if i.hp>0:
                print('%s使用普通攻击' % i.name)
                i.attack_to(p)
        
        if p.hp<=0 :
            print('玩家阵亡,憨批们获胜')
            break
        
        if ms[0].hp<=0 and ms[1].hp<=0 and ms[2].hp<=0:
            print('憨批们已全部阵亡，玩家获胜')
            break
        else:
            for j in ms:
                if j.hp<=0:
                    print('%s阵亡' % j.name)
        round+=1

if __name__ == "__main__":
    main()
