""" 多进程
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start=time()
    p1=Process(target=download_task,args=('skrrrrr.apk', ))
    p2=Process(target=download_task,args=('ruaaaaa.aspx', ))
    p1.start()
    p2.start()
    # join方法表示等待进程执行结束
    p1.join()
    p2.join()
    end=time()
    print('总共耗费了%.2f秒.' % (end-start))

if __name__ == "__main__":
    main()

"""

"""
from multiprocessing import Queue,Process
from time import sleep

count=0

def sub_task(string):
    global count
    while count<10:
        print(string,flush=True)
        count+=1
        sleep(0.01)
    
def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()

if __name__ == "__main__":
    main()
"""

""" 多线程
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

if __name__ == '__main__':
    main()

"""

"""继承Thread类来创建自定义的线程类

from random import randint
from threading import Thread
from time import time,sleep

class DownLoadTask(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename=filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download=randint(5,10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒' % (self._filename,time_to_download))

def main():
    start=time()
    t1=DownLoadTask('skrrr.apk')
    t1.start()
    t2=DownLoadTask('6666.apk')
    t2.start()
    t1.join()
    t2.join()
    end=time()
    print('总共耗费了%.2f秒.' % (end-start))

if __name__ == "__main__":
    main()
"""

