UJS信息门户模拟登陆
=================
！！！由于接口和页面改动，时间有限暂时不做修改！
！！！目前为不可用状态
登陆原理
-------

先对当前session获取验证码，用户输入用户名和密码之后，于/userPasswordValidate.portal取得iPlanetDirectoryPro的Cookie即可

文件说明
-------

* conf.py
    相关配置

* ujs_login.py
    模拟登陆的主程序

* get_captcha.py
    用于抓取验证码，本想着用于训练自动验证码识别

* ./captcha
    用于保存验证码图片

改进
----

* 本想用于监控成绩信息，但当前无法查看，之后再补
* 使用cookielib?
* 验证码错误或登陆错误处理
* 抓取课表并到公众号功能