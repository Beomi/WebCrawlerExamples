import requests

with requests.Session() as s:
    dic = {
        'suwon': 'univ!'
    }
    res = s.post('http://httpbin.org/post', data=dic)
    print(res.text)
