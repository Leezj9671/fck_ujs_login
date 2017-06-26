'''
UJS信息门户的模拟登陆
'''
import re
import random
import requests
from time import sleep
from PIL import Image
from conf import number, pwd

url = 'http://my.ujs.edu.cn'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
}

data = {
    'Login.Token1': number,
    'Login.Token2': pwd,
    'captchaField': 'xxxx',
}

session = requests.session()

# 用于获取验证码
def get_captcha():
    captcha_url = url + '/captchaGenerate.portal?s={}'.format(random.random())
    r = session.get(captcha_url, headers=headers)
    with open('./captcha/captcha_{}.jpg'.format(number), 'wb') as f:
        f.write(r.content)
        f.close()
    try:
        im = Image.open('./captcha/captcha_{}.jpg'.format(number))
        im.show()
        im.close()
    except IOError:
        print('NO CAPTCHA IMAGE')
        return False
    data['captchaField'] = input('Captcha:')
    return True

#登陆模块
def login():
    login_url = url + "/userPasswordValidate.portal"
    res_up = session.post(login_url, data=data, headers=headers)
    #获取iPlanetDirectoryPro Cookie
    ip_cookie = res_up.headers['Set-Cookie'].split(';')[0]
    ip_cookie = ip_cookie.split('=')[1]
    if ip_cookie == '':
        print('ERROR')
        return
    headers['Cookie'] = 'iPlanetDirectoryPro=' + ip_cookie
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    res = session.get(url + "/index.portal", headers=headers)
    print(res.headers)
    print(res.text)

if __name__ == '__main__': 
    if get_captcha():
        login()