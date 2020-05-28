'''
@Description: 多多进宝测试
@Author: Chenhao Xing
@Email: axchtzon@gmail.com
@Date: 2020-05-27 01:07:00
@LastEditTime: 2020-05-28 14:58:14
@LastEditors: Dragon
'''
from bs4 import BeautifulSoup  # 网页解析·获取数据
import re  # 正则表达式·进行文字匹配
import urllib.request
import urllib.error  # 指定URL·获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLLite数据库操作
import xlwt


def main():
    baseurl = "https://jinbao.pinduoduo.com/goods-db/plan"
    # 1.爬取网页
    html = askUrl(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('span'):
        # print(item)
        data = []
        item = str(item)
        print(item)
        # 电影名

    
    # for item in soup:
    #     print(item)
    # print(html)

def askUrl(url):
    head = {
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37"
    }
    html = ""
    req = urllib.request.Request(url=url, headers=head)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")

    return html






if __name__ == "__main__":
    # 调用函数
    main()

