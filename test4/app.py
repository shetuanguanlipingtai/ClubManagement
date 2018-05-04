# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

is_login = False
username = ''


@app.route('/',methods=['GET','POST'])
def home():
    global is_login
    global username
    if is_login:
        return render_template('首页.html', title_words='欢迎回来，%s！' % username, isLogin=True)
    else:
        return render_template('首页.html', title_words='你好,请登录', isLogin=False)


@app.route('/sign_in',methods=['GET'])
def sign_in_g():
    return render_template('登录.html')


@app.route('/sign_in', methods=['POST'])
def sign_in_p():
    global username
    global is_login
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('首页.html', title_words='欢迎回来，%s！' % username, isLogin=True)
    return render_template('登录.html', message='用户名或密码错误')


@app.route('/profile', methods=['GET'])
def profile():
    global is_login
    return render_template('个人信息.html')


@app.route('/inquiry', methods=['GET'])
def inquiry():
    return render_template('信息查询.html')


@app.route('/my_club', methods=['GET'])
def register():
    return render_template('我的社团.html')




if __name__ == '__main__':
    app.run()
