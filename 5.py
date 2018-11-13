from urllib import request
url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-710495.png'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
ii={'ff':'11','ff':'sssss'}
for i in ii['ff']:
    print(i)