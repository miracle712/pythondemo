import _thread
import time

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
