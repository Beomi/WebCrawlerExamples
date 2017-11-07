import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://naver.com')
html = req.text

soup = bs(html, 'lxml')

newest_list = soup.select(
    'div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'
)

for i in newest_list:
    print(i.text)
