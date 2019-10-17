
""" 使用requests库下载网络图片
from time import time
from threading import Thread

import requests

class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp=requests.get(self.url)
        with open('Learning-Python-100-Days/day14/images/'+filename,'wb') as f:
            f.write(resp.content)

def main():
    resp=requests.get('http://api.tianapi.com/nba/?key=b5030c60e54423584d03cb187cd66f52&num=10')
    data=resp.json()
    for d in data['newslist']:
        url=d['picUrl']
        DownloadHanlder(url).start()
            
if __name__ == "__main__":
    main()
"""

""" 提供时间日期的服务器（单线程）
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime
def main():
    server=socket(family=AF_INET,type=SOCK_STREAM)
    server.bind(('192.168.0.196',6969))
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        client,addr=server.accept()
        print(str(addr)+'连接到了服务器.')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()
if __name__ == "__main__":
    main()
"""

""" 向连接的客户端发送文件（多线程）（与目录下的client.py文件搭配食用为佳）
from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():
    class FileTransferHandler(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient=cclient

        def run(self):
            my_dict={}
            my_dict['filename']='ss.txt'
            my_dict['filedata']=data
            json_str=dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server=socket()
    server.bind(('192.168.0.196',6969))
    server.listen(512)
    print('服务器启动开始监听...')
    with open('Learning-Python-100-Days/day14/images/ss.txt','rb') as f:
        data=b64encode(f.read()).decode('utf-8')
    while True:
        client,addr=server.accept()
        print(str(addr)+'连接到了服务器.')
        FileTransferHandler(client).start()


if __name__ == "__main__":
    main()
"""

""" 发送邮件（被当作垃圾邮件辽）
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender='zcd0313@126.com'
    receivers='875759270@qq.com'
    message=MIMEText('使用python发送邮件','plain','utf-8')
    message['From']=Header('詹昌达','utf-8')
    message['To']=Header('詹昌达','utf-8')
    message['Subject']=Header('''
    示例代码实验邮件啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
    就让俺试试吧555555555
    ''','utf-8')
    smtper=SMTP('smtp.126.com')
    smtper.login(sender,'ABC123')
    smtper.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功！')

if __name__ == "__main__":
    main()
"""

"""  发送带附件的邮件(未尝试，需要修改)
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    
    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/Hao/Desktop/hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/Hao/Desktop/汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)
    
    # 创建SMTP对象
    smtper = SMTP('smtp.126.com')
    # 开启安全连接
    # smtper.starttls()
    sender = 'abcdefg@126.com'
    receivers = ['uvwxyz@qq.com']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, 'secretpass')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')


if __name__ == '__main__':
    main()

"""

"""发送短信（互亿无线，未尝试）
import urllib.parse
import http.client
import json


def main():
    host  = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({'account': '你自己的账号', 'password' : '你自己的密码', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '接收者的手机号', 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()

"""

