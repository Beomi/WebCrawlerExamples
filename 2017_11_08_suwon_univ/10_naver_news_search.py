import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4,la;q=0.2,da;q=0.2',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'cache-control': 'no-cache',
    'authority': 'search.naver.com',
    'referer': 'https://www.naver.com/',
}

params = (
    ('query', '수원대학교'),
)

res = requests.get('https://search.naver.com/search.naver', headers=headers, params=params)

soup = bs(res.text, 'lxml')
search_links = soup.select('a._sp_each_title')
for link in search_links:
    print(link.text)
