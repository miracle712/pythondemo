import io
import sys
import random



jiqiren = ['剪刀','石头','布']

win = [['剪刀','布'],['石头','剪刀'],['布','石头']]

computer = random.choice(jiqiren)

me = input('请出拳：')
if (computer == me):
    print("平局啦")
elif ([computer,me] in win):
    print("你输了")
else:
    print("你赢了")
print('电脑出的是：',computer)


