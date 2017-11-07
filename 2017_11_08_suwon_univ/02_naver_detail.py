import requests

req = requests.get('http://naver.com')

print(dir(req))
print(req.headers)
print(req.url)
print(req.ok)
print(req.history)
print(req.status_code)
