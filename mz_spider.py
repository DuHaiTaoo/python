# -*-coding:utf-8;-*-


import requests
from bs4 import BeautifulSoup
import os


route = r'{0}\img'.format(os.getcwd())
if not os.path.exists(route):
    print(1)
    os.makedirs(route)
headers = {'Referer': 'http://www.mzitu.com', 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url, headers=headers)
# print(start_html.text)
Soup = BeautifulSoup(start_html.text, 'lxml')
all_a = Soup.find('div', class_='all').find_all('a')
for a in all_a[1:]:
    # print(a)
    title = a.get_text()
    href = a['href']
    print(title, href)
    html = requests.get(href, headers=headers)
    print(href)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    # print(html_Soup)
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    if not os.path.exists(r'{0}\{1}'.format(route, title)):
        print(1)
        os.makedirs(r'{0}\{1}'.format(route, title))
    for page in range(1, int(max_span)+1):
        page_url = '{0}/{1}'.format(href, page)
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src']
        headers['Referer'] = href
        img = requests.get(img_url, headers=headers)
        with open(r'{0}\{1}\{2}.jpg'.format(route, title, page), 'wb') as f:
            f.write(img.content)
