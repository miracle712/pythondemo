import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


'''

a = 5
b = 5
c = a // b
print (c)

print ('ru\noob')
print (r'ru\boob')

students = {'tom','sfs','kim','tom','ff'}
print(students)

if 'sfs' in students:
    print('sfs:1')
else:
    print('sfs:2')

w = set('safasfaadf')
e = set('sasedgggfhh')
print(w)
print(w - e)
print(w | e)
print(w & e)
print(w ^ e)


if True:
    print ("answer")
    print ("true")
else:
    print ("answer")
    print ("flase")

'''
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


dict = {'name': '1','age': '18','class': 'first'}
dict['age'] = 20
dict['class'] = "two"

print("dict['age']:",dict['age'])
print("dict['class']:",dict['class'])

basket = {'apple','pear','orange','pear','banana'}
print(basket)
n = 'pea' in basket
print(n)
a = set('abcdcdsab')
b = set('abcbbabst')
print(a)
t = a - b
print(t)
w = a | b
print(w)
r = a ^ b
print(r)

thisset = set(("google","noonble","kile","ool"))
eeee = len(thisset)
print(eeee)
www = thisset.pop()
print("www随机删除的数组是：",www)
eee = len(thisset)
print(eee)
aaa = "google" in thisset
print(aaa)
qqq = thisset.add("add")
print(thisset)


u, i = 0, 1
while(i < 10):
    print(i)
    u, i = i, u+i

o, p = 0, 1
while(p < 100):
    print(p,end = ",")
    o, p = p, o+p



import turtle as t
t.goto(100,0)
for y in range(100):
    t.left(80)
    t.fd(100)
    t.left(135)
    t.fd(165)
    t.left(125)
    t.fd(115)


name = 0
if name == 0:
    print ('shigeling')
elif name < 0:
        print ('xiaoyu0')

count = 0
while (count < 5):
    print (count,"is less than 5")
    count = count + 1
else:
    print (count,'is less than 5')

for letter in 'python':
    print ("当前字母：",letter)

    fruits = ['banna','apple','pear']
    for fruit in fruits:
        print ("当前水果：",fruit)


for k in range(9,0,-1):
    for l in range(k,0,-1):
        e = k * l
        print('%d*%d = %-2d'%(k,l,e),end = ' ' )
    print("\n")


counter = 0
for o in range(1,5):
    for p in range(1,5):
        for u in range(1,5):
            if o!=p and o!=u and p!=u:
                print("{}{}{}".format(o,p,u),end=" ")
                counter += 1
print("")
print("共有{}种".format(counter)) 
'''

for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print('%d*%d = %-2d'%(i,j,d),end = ' ' )
    print()

'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) +" * "+str(j)+" = "+str(i*j),end =" ")
    print("\n")




counter = 0
for o in range(0,10):
    for p in range(0,10):
        for u in range(0,10):
            print("{}{}{}".format(o,p,u),end=" ")
            counter += 1
print("")
print("共有{}种".format(counter)) 

turle = (50,14,'igm','ff')
print('这数组是：',turle)
print('turle[0]=',turle[0])



a = 1
while(a < 7):
    if(a % 2 == 0):
        print(a,"是odd")
    else:
        print(a,"是even")
    a += 1


age = int(input("请输入你家狗狗的年龄："))
print("")
if(age <= 0):
    print("你在逗我呢！")
elif age == 1:
    print("你家狗狗的年龄相当于是14岁")
elif age == 2:

    print("你家狗狗的年龄相当于是24岁")
elif age > 2:
    human = 22 + (age -2)*5
    print("你家狗狗的年龄相当于是:",human)

input("点击enter退出")


number = 7
guess = 1
print("数字猜谜游戏开始！")
while(guess != number):
    guess = int(input("请输入你猜的数字："))
    if(guess == number):
        print("恭喜你才对了！")
    elif guess < number:
        print("你猜的数字小了")
    elif guess > number:
        print("你猜的数字大了")
        

a = 1
while a < 10:
    print(a)
    a += 2

num = 100
sum = 0
count = 1
while count <= num:
    sum = sum +count
    count += 1
    print("1到 %d 之间的和是：%d" % (num,sum))


var = 1
while var == 1:
    num = int(input("输入一个数字："))
    print("你输入的数字是:",num)
    print("good bye!")


count = 0
while count < 5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于等于5")

langude = ["dad","rr","oo","pp"]
for m in langude:
    print(m)

qu = ["ww","uu","tt","ii"]
for a in range(len(qu)):
    print(a,qu[a])

    

list = [1,2,3,4]
i = iter(list)
print(next(i))
print(" ")


textlist = [5,6,7,8,9]
it = iter(textlist)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


class mm:
  def __iter__(self):
      self.a = 1
      return self

  def __next__(self):
      x = self.a
      self.a += 1
      return x

mmm = mm()
mmmm = iter(mmm)

print(next(mmmm))
print(next(mmmm))
print(next(mmmm))
print(next(mmmm))
print(next(mmmm))
print(next(mmmm))
print(next(mmmm))
print(next(mmmm))


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter >n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
        
    
def area(height,width):
    return height * width
w = 4
h = 5
print("width =", w, "height =", h, "area =",area(w, h))

def changename(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值：",mylist)

mylist = [10,20,30]
changename(mylist)
print("函数外取值：",mylist)


def studen(name, age):
    print("姓名叫：",name)
    print("年龄是:",age)
    return
studen(name="李四",age=25)



a = [1,2,3,3,3,8,4,6,1.3]
print(a.count(3), a.count(1), a.count(5))
a.insert(2,-1)
a.append(5)
print(a)
print(a.index(3))
a.remove(1)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
del a[0]
print(a)
del a[2:4]
print(a)

元组

t = 123, 5421, 'hello'
print(t[0])



print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为：',sys.path, '\n')

def fun_hun( par):
    print("hello:", par)
    return

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end='')
        a, b = b, a+b
        print()
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
       result.append(b)
       a, b = b, a+b
       return result
       print(result)


def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

s = 'heelo, foof'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 2.5
y = 20 * 3.5
s = 'x的值为：' + repr(x) + ', y的值为：' + repr(y) + '...'
print(s)


import math

for x in range(1,11):
    print(repr(x).rjust(2),repr(x * x).rjust(3),repr(x * x *x).rjust(4))

o = '12'.zfill(4)
print(o)
w = '3.14159265359'.zfill(7)
print(w)

print('常量PI的值近似等于：{}。'.format(math.pi))

print('{}网址："{}!"'.format('菜鸟教程','www.shsusu'))


strs = input('请输入:');
print('你输入的内容是：', strs)



f = open('/demo/foo.txt',"w")
f.write('python是一门非常好的语言。 \n是的，的确非常好！\n')
f.write('ddadadada')
f.close()

f = open('/demo/foo.txt',"r")
str = f.read()
print(str)
f.close()

f = open('/demo/foo.txt',"r")
str = f.readlines()
print(str)
f.close()


a = 'ABC'
b = a
a = 'XYZ'
print(b)

'''
