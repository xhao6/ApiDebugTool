# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Required, DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
url = "https://cloudcn.v5.cn"
server = "http://127.0.0.1:5001"
api_error_message = u"输入错误，请检查接口参数"


class CategoryForm(Form):
    api_name = SelectField(u'Step.1 选择调试接口', choices=[('get_token', u'OAuth2 Token 获取'), ('create_user', u'创建用户'),
                ('refresh_session', u'刷新用户 SessionID'),('update_user', u'更新用户信息'), ('create_group', u'创建群组'),
                ('update_group', u'更新群组'), ('group_info', u'获取群组信息'), ('join_group', u'加入群组'),
                ('remove_user_from_group', u'将用户从群组中移除'), ('exit_group', u'解散或退出群组')])
    submit = SubmitField(u'下一步')


class ParameterGetTokenForm(Form):
    app_id = StringField(u'Step.2 输入API参数：</br ></br >appid:', validators=[Required()])
    secret = StringField('secret:', validators=[Required()])
    submit = SubmitField(u'测试')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/opendoc', methods=['GET', 'POST'])
def opendoc():
    return render_template('opendoc.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    # url = "https://cloudcn.v5.cn"

    category_form = CategoryForm()
    if category_form.validate_on_submit():
        if category_form.api_name.data == 'get_token':
            return redirect(url_for('param_get_token'))
    return render_template('index.html', form=category_form, data = data)

# "app_id": "203228",
# "app_secret": "fbe54068c5eafd5262ff169a1682cca2"


@app.route('/param/token', methods=['GET', 'POST'])
def param_get_token():
    response = ''
    form = ParameterGetTokenForm()
    if form.validate_on_submit():
        app_id = form.app_id.data
        secret = form.secret.data
        data = {"app_id": app_id ,"app_secret": secret}
        request_url = server + '/api/token'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('param_get_token.html', form = form, response = response)



if __name__ == '__main__':
    manager.run()
