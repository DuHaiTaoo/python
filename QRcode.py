#!/usr/bin/env python3
# -*-coding:utf-8;-*-


'''
    接口：http://www.liantu.com
    作者：cold-mo
    github：https://github.com/cold-mo/python
    
'''


import requests


def QRcode(text, **kw):
    '''
        根据text参数内容返回图片数据
        可选参数：
        bg：背景颜色
        fg：前景颜色
        el：纠错等级 h\\q\\m\\l
        w： 尺寸大小（像素）
        m： 外边距（像素）
        logo：logo图片地址
    '''
    url = 'http://qr.liantu.com/api.php?text={0}'.format(text)
    image = requests.get(url, params=kw)
    return image.content


if __name__ == '__main__':
    image = QRcode('dht', fg='ff0000', bg='ffffff')
    try:
        f = open('QRcode.jpg', 'wb')
        f.write(image)
    finally:
        f.close()
