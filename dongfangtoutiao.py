import requests
from urllib.parse import urlencode
import json
import re

def get_page_detail(pageNumber,keyWord):
    data = {
        #分页加载默认一页五条数据
        'callback': 'jQuery18308665374998856634_1526290762213',
        'type': keyWord,
        'pgnum': pageNumber,
    }
    #包装参数
    params = urlencode(data)
    #爬取的主网址
    base = 'http://pcflow.dftoutiao.com/toutiaopc_jrtt/newspool'
    url = base + '?' + params
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            token = re.findall(r"{.*}", response.text)
            return token
        return None
    except ConnectionError:
        print('connection error')
        return None

def parse_page_index(html):
    data = json.loads(html[0])
    if data and 'data' in data.keys():
        for item in data.get('data'):
            print(item.get('miniimg'))
            print(item.get('topic'))
            print(item.get('source'))
            # for imagedata in item.get('miniimg'):
            #     # print(imagedata)
            #     print(imagedata.get('src'))
            # # print(item.get('miniimg'))


def main():
    html = get_page_detail('1','yule')
    if html:
        parse_page_index(html)


if __name__ == '__main__':
    main()