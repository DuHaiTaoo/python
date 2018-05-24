#!/usr/bin/env python3
#-*-coding:utf-8;-*-


import xlrd
import urllib.request
import re
import sys
import os



def dht():
    print('this is cold-mo first use github!')

def dhtExhaustionFolder(Folder):
    for i in os.walk(Folder):
        for n in i[2]:
            print (n)


    #[n.split('.')[0] for i in os.walk(path) for n in i[2]]


if __name__ == '__main__':
    #dht()
    dhtExhaustionFolder('D:\\python\\')
