import requests
import re

#选课页面url
base_url = 'http://xk2.ujs.edu.cn/'
xuehao = '3140604015'
# post需要的参数
data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '',
    # 学年
    'xnd': '2017-2018',
    # 学期
    'xqd': '1'
}
headers = {
    'Cookie': "AQIC5wM2LY4SfczNXcaamwn7ZOswoiiUpGwu43yTohk4Tcc%3D%40AAJTSQACMDI%3D%23",
    'Referer': 'http://my.ujs.edu.cn/index.portal?.pn=p2365',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
ss = requests.session()

def get_courses(iplanetcookie):
    headers['Cookie'] = iplanetcookie
    resp = ss.get(base_url + 'default_zzjk.aspx/jstjkb_jzjk.aspx', headers=headers)
    if '信息门户登陆' in resp.text:
        print('log error')
        return False
    print(resp.text)
    course_herf = re.findall("班级推荐课表(.*?)<a href=\"(.*?)\" target=(.*?)>学生个人课表", resp.text)[0][1]
    if course_herf is None:
        print('get course_herf error')
        return False
    print(course_herf)

    # 增加头
    headers['Referer'] = base_url + 'xs_main_zzjk1.aspx?xh={}&type=1'.format(xuehao)
    resp = ss.get(base_url + course_herf, headers=headers)
    print(resp.text)
    data['__VIEWSTATE'] = re.findall('<input type="hidden" name="__VIEWSTATE" value="(.*?)" />', resp.text)
    print(data['__VIEWSTATE'])
    resp = ss.post(base_url + course_herf, headers=headers, data=data)
    # table Xpath: //*[@id="xskb_form"]/div/div/span
    print(resp.text)

if __name__ == '__main__':
    get_course()
