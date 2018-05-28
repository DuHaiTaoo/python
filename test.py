#!/usr/bin/env python3
# -*-coding:utf-8;-*-


from prettytable import PrettyTable
import requests
import re


if __name__ == '__main__':
    header = {'user-agent': 'Mozilla/5.0'}
    r = requests.get('https://dianying.taobao.com/showList.htm?n_s=new', headers=header)
    data = r.content.decode()
    a = '''<div class="movie-card-wrap">.*?<a href="https://dianying.taobao.com/showDetail.htm?showId=(.*?)&amp;n_s=new&amp;source=current" class="movie-card">.*?<div class="movie-card-tag"><i class="t-201"></i></div>.*?<div class="movie-card-poster">.*?<img width="160" height="224" data-src="(.*?)" src="(.*?)">.*?</div>.*?<div class="movie-card-name">.*?<span class="bt-l">(.*?)</span>.*?<span class="bt-r">(.*?)</span>.*?</div>.*?<div class="movie-card-info">.*?<div class="movie-card-mask"></div>.*?<div class="movie-card-list">.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*？</div>.*？</div>.*?</a>.*?<a href="https://dianying.taobao.com/showDetail.htm?showId=(.*?)&amp;n_s=new" class="movie-card-buy">选座购票</a>.*?</div>'''
    match = re.match(a, data)
    print(type(match))