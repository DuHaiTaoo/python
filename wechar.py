import time
import requests
import re


headers = {
        'Host': 'login.wx.qq.com',
        'Referer': 'https://wx.qq.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }


def get_QRuuid():
    
    data = {
        'appid': 'wx782c26e4c19acffb',
        'redirect_uri': 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
        'fun': 'new',
        'lang': 'zh_CN',
        '_': str(int(time.time()))
    }
    a = requests.get('https://login.wx.qq.com/jslogin', params=data, headers=headers)
    a = re.match('window.QRLogin.code = (.*?)?; window.QRLogin.uuid = "(.*?)";', a.text)
    if type(a) == 'NoneType':
        return ''
    return uuid = a.group(2)




uuid = get_QRuuid()
