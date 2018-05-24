#-*-conding:UTF-8 -*-


import xlrd
import urllib.request
import re
import sys
import os



def readxls(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheets()[0]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    a = [table.row_values(i)[0] for i in range(nrows)]
    return a

def getHtml(url,fileName):
    #req = urllib.request.Request(url)
    #html = urllib.request.urlopen(req)
    #html = page.read()
    #print (html)
    #return html
    b = r'{0}.png'.format(fileName)
    urllib.request.urlretrieve(url,b)
    


if __name__ == '__main__':
    '''
    excelFile = r'D:\dht\1.xls'
    data = readxls(excelFile)
    '''
    path=r'D:\dht1'
    '''
    for i in os.walk(path):
        #print(len(i[2]))
        for n in i[2]:
            print(n.split('.')[0])
    '''
    data = [n.split('.')[0] for i in os.walk(path) for n in i[2]]
    for a in data:
        url = r'https://barcode.tec-it.com/barcode.ashx?data={0}&code=Code128&dpi=96&dataseparator='.format(a)
        getHtml(url,a)
        
        
    
    
