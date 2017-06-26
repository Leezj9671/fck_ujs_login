'''
抓取验证码
'''
from random import random
import requests

session = requests.session()
url = 'http://my.ujs.edu.cn'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
}
rd = random()

for i in range(1000):
    captcha_url = url + '/captchaGenerate.portal?s={}'.format(rd)
    r = session.get(captcha_url, headers=headers)
    with open('./captcha/{}.jpg'.format(i+1), 'wb') as f:
        f.write(r.content)
        f.close()