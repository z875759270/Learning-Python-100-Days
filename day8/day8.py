# %%
"""
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Study(self, courseName):
        print("%s正在学习%s." % (self.name, courseName))

    def WatchTV(self):
        if self.age<=18:
            print('未成年')
        else:
            print('成年')


def main():
    stu=Student('牛嗷',20)
    stu.Study("learning Python")
    stu.WatchTV()


if __name__ == "__main__":
    main()
"""

# %%
""" test1 定义一个类描述闹钟 """
"""
from time import sleep
class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        print("%02d:%02d:%02d" % (self.hour, self.minute, self.second))

def main():
    c = Clock(9, 1, 1)
    while True:
        c.show()
        c.run()
        sleep(1)


if __name__ == "__main__":
    main()
"""

# %%
""" 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def MoveTo(self, x, y):
        self.x = x
        self.y = y

    def GetDistance(self, other):
        x1, x2, y1, y2 = int(self.x), int(other.x), int(self.y), int(other.y)
        res = ((x1-x2)**2+(y1-y2)**2)**0.5
        return res

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(15, 13)
    p2 = Point(1, 56)
    p2.MoveTo(2, 2)
    print(p1.GetDistance(p2))
    print(p2)

if __name__ == "__main__":
    main()
"""
