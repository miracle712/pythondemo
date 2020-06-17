import _thread
import time
import isort

'''
def print_thread( ThreadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( ThreadName,time.ctime(time.time())))
try:
    _thread.start_new_thread( print_thread, ("Thread-1",2,))
    _thread.start_new_thread( print_thread, ("Thread-2",2,))
except:
    print("Error:无法启动线程")
    

while 1:
    pass

'''
'''
print("hello python")

counter = 100  #整数型
miles = 5.0    #浮点型变量
name = "nancy"  #字符串

print(counter)
print(miles)
print(name)


x = input('请输入一个字符串')
print(x[-1] + "宋永宇")


a = 1
b = 'python'
c = ['1','2','3']

str(a)

print(a)
print(b + '\nhello')

print(c[1:3])

d = set()
print(d)
d = {'a','b','c','d','e','f'}

print(d)

d.remove('c')

print(d)

dict = {'key1': 'name', 'value1': '张三', 'key2': 'sex', 'value2': '男'}
print(dict)
print(dict.keys())
print(dict.values())

'''
'''
number = 7
guess = 0
print('数字猜谜游戏')
while guess != number:
    guess = int(input('请输入你猜的数字：'))
    if guess == number:
        print('恭喜你猜对了')
    elif guess < number:
        print('猜小了')
    elif guess > number:
        print('猜大了')
'''
'''
a = 33
b = 11
c = 22
t1 = 0 
t2 = 0
t3 = 0

if b < c and b < a:
    t1 = b
    print('a=',b)
if c > b and c < a:
    t2 = c
    print('b=',c)
if a > b and a > c :
    t3 = a
    print('c=',a)

'''

'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    print('1到 %d 之和为：%d' % (n,sum))
    print('多少次：',counter)
'''
'''
for i in range(7):
    print(" "*(6-i),end="")
    print(" * "*(i+1))

'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) +"*"+str(j)+"="+str(i*j),end =" ")
    print("\n")