from urllib.parse import urlencode
import requests
import json
from bs4 import BeautifulSoup
import re

#获取页面内容的接口
def get_page_index(offset, keyword):
    #request param
    data = {
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'format': 'json',
        'keyword': keyword,
        'offset': offset,

    }
    #包装参数
    parms = urlencode(data)
    #爬取的网址
    base = 'http://www.toutiao.com/search_content/'
    #网址加参数
    url = base + '?' + parms
    session = requests.session()
    #捕获异常
    try:
        #获取请求的相应
        response = session.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('error occurred')
        return None

def parse_page_index(html):
    #获取html中的json字符串
    data = json.loads(html)
    #找出json串中的‘data’key对应的value----》data
    if data and 'data' in data.keys():
        #将data数据中的‘data’数据找出
        for item in data.get('data'):
            #获取打key为‘article_url’的value
            yield item.get('article_url')

def get_page_detail(url):
    session = requests.session()
    header_dict = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    # session.headers.get(header_dict)
    # session.headers.keys(header_dict)
    try:
        response = session.get(url)
        if response.status_code == 200:
            print(response.text)
            return response.text
        return None
    except RecursionError:
        print('请求错误',url)
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(images_pattern,html)
    if result:
        a = result.group(1)
        print(result.group(1))

def main():
    html = get_page_index(0,'街拍')
    print(html)
    for url in parse_page_index(html):
        print(url)
        html = get_page_detail(url)

if __name__ == '__main__':
    main()


