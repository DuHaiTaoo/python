#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  
sys.setrecursionlimit(1000000) 

list_a = []
list_b = []
list_c = []
n = 0
d = {
    'A':list_a,
    'B':list_b,
    'C':list_c,
    }

def init(number,a,b,c):
    global list_a,list_b,list_c
    for i in range(number):
        list_a.insert(0,i+1)
    print ('初始化完成，共有{0}层'.format(number))
    
def main(number,a,b,c):
    global list_a,list_b,list_c
    init(number,a,b,c)
    recursion(number,a,b,c)

def recursion(number,a,b,c):
    global list_a,list_b,list_c,n,d
    if number == 1:
        n += 1
        print ('第{0}次移动'.format(n))
        #print( a, '-->', c)
        #list_a.pop(len(list_a)-1)
        
        d.get(c).append(d.get(a).pop(len(d.get(a))-1))
        print('A:{0}\nB:{1}\nC:{2}\n'.format(list_a,list_b,list_c))
        print ('-'*20)
    else:
        recursion(number-1, a, c, b)
        recursion(1, a, b, c)
        recursion(number-1, b, a, c)

if (__name__ == '__main__'):
    a = int(input('请输入层数：'))
    main(a,'A','B','C')
