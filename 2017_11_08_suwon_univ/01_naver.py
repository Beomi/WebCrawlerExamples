import requests

req = requests.get('http://naver.com')
print(req.text)
