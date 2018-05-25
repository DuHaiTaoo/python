#!/usr/bin/env python3
#-*-coding:utf-8;-*-

'''
    By:cold-mo(cm)
'''

import xlrd
import urllib.request
import re
import sys
import os
import hashlib
import hmac


def isEmail(data):
    '''
        判断字符串或列表内容是否是邮箱地址
    '''
    if isinstance(data,list):
        a = {}
        for i in data: 
            if str(re.match(r'([\.a-z0-9A-Z]+?@[0-9a-zA-Z]+?\.[0-9a-zA-Z]+)',str(i))) != 'None':
                a[i] = True
            else:
                a[i] = False
        return a
    if isinstance(data,str):
        if str(re.match(r'([\.a-z0-9A-Z]+?@[0-9a-zA-Z]+?\.[0-9a-zA-Z]+)',str(data))) != 'None':
            return True
        else:
            return False


def calcMd5(s):
    '''
        返回字符串的md5值
    '''
    return hashlib.md5().update(s.encode('utf-8')).hexdigest()

def calcSha1(s):
    '''
        返回字符串的sha1值
    '''
    return = hashlib.sha1().update(s.encode('utf-8')).hexdigest()

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()




if __name__ == '__main__':
    
    pass