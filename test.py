#!/usr/bin/env python3
# -*-coding:utf-8;-*-


num = int(input('num:'))
print('\n'.join([' '.join([str(n) if len(str(n)) != 1 else "0{0}".format(n) for i in range(num) for n in range(i+1, i+1+num)][item*num:item*num+num]) for item in range(num)]))
