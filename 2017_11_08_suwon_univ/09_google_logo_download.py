import requests

URL = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'

headers = {
    'referer': 'https://www.google.com/',
}

res = requests.get(URL, headers=headers)

f = open('googlelogo.png', 'wb+')
f.write(res.content)
f.close()

