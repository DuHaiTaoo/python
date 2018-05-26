#!/usr/bin/env python3
#-*-coding:utf-8;-*-

from urllib import request
from prettytable import PrettyTable
import json,re

'''
    获取天气 接口：https://www.yahoo.com/news/weather/
'''

dict_mainOption = {
    '1':'weather',
    '2':'woeid',
    'q':'exit'
}



def queryWoeid(text):
    with request.urlopen('https://www.yahoo.com/news/_td/api/resource/WeatherSearch;text={0}'.format(text.encode('utf-8'))) as f:
        data = json.loads(f.read())
        if(len(data)<1):
            print('error')
            return
        else:
            print('{0}共有{1}个匹配项:'.format(text,len(data)))
        #print(len(data))
        x = PrettyTable(['woeid','国家','城市','限定名','经度','纬度'])
        for i in range(len(data)):
            #pass
            x.add_row([data[i]['woeid'],data[i]['country'],data[i]['city'],data[i]['qualifiedName'],data[i]['lon'],data[i]['lat']])
            #print('{0}.国家：{1}，城市：{2}，限定名：{3}，经度：{4}，纬度：{5}'.format(i,data[i]['country'],data[i]['city'],data[i]['qualifiedName'],data[i]['lon'],data[i]['lat']))
        print(x)
        
def weather(woeid):
    with request.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%20{0}&format=json'.format(woeid)) as f:
        data = json.loads(f.read())
        
        detail = PrettyTable(['日出','日落','湿度','能见度'])
        #print(data['query']['created'])
        sunrise = data['query']['results']['channel']['astronomy']['sunrise']
        sunset = data['query']['results']['channel']['astronomy']['sunset']
        humidity = data['query']['results']['channel']['atmosphere']['humidity']
        visibility = data['query']['results']['channel']['atmosphere']['visibility']
        forecast = data['query']['results']['channel']['item']['forecast']

        detail.add_row([sunrise,sunset,'{0}%'.format(humidity),'{0}km'.format(visibility)])
        a = PrettyTable(['日期','星期','最高温度','最低温度','天气'])
        for i in forecast:
            a.add_row([i['date'],i['day'],'{0}℃'.format(int((int(i['high'])-32)/1.8)),'{0}℃'.format(int((int(i['low'])-32)/1.8)),i['text']])
        print(detail)
        print(a)
        
        


def main():
    a = input('1.查询天气\n2.查询woeid\nQ.退出\n').lower()
    if not a in dict_mainOption:
        print('输入错误，请重新输入！')
        return

    if dict_mainOption[a] == 'exit':
        return 1

    elif dict_mainOption[a] == 'weather':
        while True:
            a = input('输入woeid查询天气，q返回主菜单').lower()
            if a == 'q':
                break
            elif a == '' or not a.isdigit():
                print('输入错误，请重新输入！')
                continue
            
            weather(a)
            break

        return()

    elif dict_mainOption[a] == 'woeid':
        data = input('输入要查询woeid的城市名拼音').lower()
        queryWoeid(data)
        return
        
    
    
    



if __name__ == '__main__':
    #queryWoeid('haikou')
    while True:
        a = main()
        if a == 1:
            break

        