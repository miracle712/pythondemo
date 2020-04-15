import io
import sys
import socket
import random
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import _thread

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

'''

import turtle as t
# 画笔为蓝色
t.color('blue')
# 画300次
for i in range(300):
# 行走的路线
    t.fd(i)
# 向左边100度画
    t.left(100)
t.done()


class MyClass:
    """一个简单的类实例"""
    i = 123456
    def f(self):
        return 'hello world'
x = MyClass()
print("myclass类的属性i为：",x.i)
print("myclass类的方法f输出为：",x.f())

class yy:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = yy(3.0, -4.5)
print(x.r, x.i)

class rr:
    def prtg(self):
        print(self)
        print(self.__class__)

t = rr()
t.prtg()
'''

'''
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
            print("%s 说：我 %d 岁，重 %d斤" %(self.name,self.age))

p = people('run',10)
p.speak()

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s 说：我 %d 岁，读 %s 年级"%(self.name,self.age,self.grade))

dddd = student('ken',10,60,'大三')
dddd.speak()

class countter:
    __secf = 0
    publss = 0
    def count(self):
        self.__secf += 1
        self.publss += 1

c = countter()
c.count()
c.count()
print(c.publss)
print(c.__secf)

'''
'''
num1 = input('输入第一个数：')
num2 = input('输入第二个数：')

sum = float(num1) + float(num2)

print('数字{0}和数字{1}相加的结果为：{2}'.format(num1,num2,sum))

a = float(input("三角形的第一边长："))
b = float(input("三角形的第二边长："))
c = float(input("三角形的第三边长："))5


s = (a+b+c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形的面积为 %0.2f' %area)
'''

'''
print(random.randint(0,10))
'''
'''
celsius = float(input('输入摄氏度：'))

fahreaheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f' %(celsius,fahreaheit))
'''
'''
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'user',
    passwd = 'passwd'
)
print(mydb)
'''
'''
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()

port = 9999

serversocket .bind((host,port))

serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()

    print("连接地址：%s" % str(addr))

    msg = '欢迎访问菜鸟教程！' + "\r\n"

    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
'''

'''
sender = 'from@runoob.com'
receivers = ['1021621765@qq.com']

message = MIMEMultipart()
message['from'] = Header("菜鸟教程",'utf-8')
message['To'] = Header("测试",'utf-8')
subject = 'Python SMTP 邮件测试'
message['subject'] = Header(subject,'utf-8')

message.attach(MIMEText('这是菜鸟教程测试邮件发送','plain','utf-8'))

att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'

att1["(Content-Disposition)"] = 'attachment;filename="test.txt"'

message.attach(att1)

att2 = MIMEText(open('runoob.txt','rb').read(),'base64','utf-8')
att2["Content-Type"] = 'application/octet-stream'

att2["(Content-Disposition)"] = 'attachment;filename="runoob.txt"'

message.attach(att2)

try:
    smtobj = smtplib.SMTP('localhost')
    smtobj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('error:无法发送邮件')

    '''

    def print_time( threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % ( threadName,))