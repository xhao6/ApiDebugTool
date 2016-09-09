# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Required, DataRequired
from lib import actions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
 
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
url = "https://cloudcn.v5.cn"
api_error_message = u"输入错误，请检查接口参数"
# api_name_choices = {'basic': [('get_token', u'OAuth2 Token 获取')],
#                     'user': [('create_user', u'创建用户'), ('refresh_session', u'刷新用户 SessionID'),
#                              ('update_user', u'更新用户信息')],
#                     'group': [('create_group', u'创建群组'), ('update_group', u'更新群组'), ('group_info', u'获取群组信息'),
#                               ('join_group', u'加入群组'), ('remove_user_from_group', u'将用户从群组中移除'),
#                               ('exit_group', u'解散或退出群组')]}


class CategoryForm(Form):
    api_category = SelectField(u'一、接口类型', choices=[('server_category', u'服务端 REST API'),
                ('user_category', u'用户管理'), ('group_category', u'群组管理')], validators=[DataRequired(message=u"类型不能为空")])
    api_name = SelectField(u'二、接口列表', choices=[('get_token', u'OAuth2 Token 获取'), ('create_user', u'创建用户'), ('refresh_session', u'刷新用户 SessionID'),
                ('update_user', u'更新用户信息'), ('create_group', u'创建群组'),('update_group', u'更新群组'),
                ('group_info', u'获取群组信息'), ('join_group', u'加入群组'), ('remove_user_from_group', u'将用户从群组中移除'),
                ('exit_group', u'解散或退出群组')])
    app_id = StringField(u'三、参数列表：</br ></br >appid:', validators=[Required()])
    secret = StringField('secret:', validators=[Required()])
    submit = SubmitField('Submit')


# class NewForm(Form):
#     api_category = SelectField(u'一、接口类型', choices=[('server_category', u'服务端 REST API'),
#                                                    ('user_category', u'用户管理'), ('group_category', u'群组管理')])
#     api_name = SelectField(u'二、接口列表')
#     app_id = StringField(u'三、参数列表：</br ></br >appid:', validators=[Required()])
#     secret = StringField('secret:', validators=[Required()])
#     submit = SubmitField('Submit')


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
    url = "https://cloudcn.v5.cn"

    category_form = CategoryForm()
    if category_form.validate_on_submit():
        app_id = category_form.app_id.data
        secret = category_form.secret.data
        if category_form.api_name.data == 'get_token':
            url = url + "/oauth/token"
            response = actions.get_token_test(url, app_id, secret, "client_credentials", "header")
            data = u"获得的token为： %s" % (response)
        # return redirect(url_for('index'))
    return render_template('index.html', form=category_form, data = data)

# "app_id": "203228",
# "app_secret": "fbe54068c5eafd5262ff169a1682cca2"


@app.route('/api/helloworld')
def hello():
    return 'helloworld'


@app.route('/api/token', methods=['POST'])
def token():
    url_token = url + "/oauth/token"
    grant_type = "client_credentials"
    app_id = request.form.get("app_id")
    secret = request.form.get("app_secret")

    try:
        response = actions.get_token_test(url_token, app_id, secret, grant_type, "header")
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/user/create', methods=['POST'])
def create_user():
    print "Testing API for create users..."
    app_user_id = request.form.get('app_user_id')
    token = request.form.get('token')
    token = eval(token)
    url_create_user = url + "/open/api/user/auth?"
    nickname = request.form.get('nickname')
    if not nickname:
        nickname = "Default"
    print "app_user_id: %s\ntoken: %s\nurl_create_user: %s" % (app_user_id, token, url_create_user)

    try:
        response = actions.get_userId_sessionId_test(token, url_create_user, app_user_id, nickname)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/user/session', methods=['POST'])
def update_session():
    print "Testing API for update session..."
    app_user_id = request.form.get('app_user_id')
    token = eval(request.form.get('token'))
    url_update_session = url + '/open/api/session/auth?'
    print "app_user_id: %s" % app_user_id
    print "token: %s" % token
    print 'url_update_session: %s' % url_update_session

    try:
        response = actions.get_seesionId_test(token, url_update_session, app_user_id)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/user/nickname', methods=['POST'])
def update_nickname():
    print "Testing API for update user info..."
    app_user_id = request.form.get('app_user_id')
    token = eval(request.form.get('token'))
    url_update_user = url + '/open/api/user/update'
    app_user_nick_name = request.form.get('nickname')
    session = request.form.get('session')
    print "app_user_id: %s" % app_user_id
    print "token: %s" % token
    print 'url_update_user: %s' % url_update_user

    try:
        response = actions.update_nickname_test(token, session,url_update_user, app_user_id, app_user_nick_name)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/group/create', methods=['POST'])
def create_group():
    print "Test API for create groups..."
    token = eval(request.form.get('token'))
    session = request.form.get('session')
    url_create_group = url + '/open/api/group/create'
    members = request.form.get('members')
    name = request.form.get('group_name')
    desc = request.form.get('group_description')

    print "- Token: %s" % token
    print "- Session: %s" % session
    print "- URL: %s" % url_create_group
    print "- Members: %s" % members
    print "- Group Name: %s" % name
    print "- Group Description: %s" % desc

    try:
        response = actions.create_group_test(token, session, url_create_group, members, name, desc)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/group/update', methods=['POST'])
def update_group():
    print "Test API for update group info..."
    token = eval(request.form.get('token'))
    session = request.form.get('session')
    url_update_group = url + '/open/api/group/update'
    group_id = request.form.get('group_id')
    name = request.form.get('group_name')
    desc = request.form.get('group_description')

    print "- Token: %s" % token
    print "- Session: %s" % session
    print "- URL: %s" % url_update_group
    print "- Group ID: %s" % group_id
    print "- Group Name: %s" % name
    print "- Group Description: %s" % desc

    try:
        response = actions.update_group_test(token, session, url_update_group, group_id, name, desc)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/group/get', methods=['POST'])
def get_group_info():
    print "Test API for get group info..."
    token = eval(request.form.get('token'))
    session = request.form.get('session')
    url_get_group_info = url + '/open/api/group/get?'
    group_id = request.form.get('group_id')
    detail = request.form.get('detail')

    print "- Token: %s" % token
    print "- Session: %s" % session
    print "- URL: %s" % url_get_group_info
    print "- Group ID: %s" % group_id
    print "- Group Details: %s" % detail

    try:
        response = actions.get_group_infor_test(token, session, url_get_group_info, group_id, detail)
        return str(response)
    except Exception,e:
        print str(e)
        return api_error_message


@app.route('/api/group/join', methods=['POST'])
def join_group():
    print "Test API for join groups..."
    token = eval(request.form.get('token'))
    session = request.form.get('session')
    url_join_group = url + '/open/api/group/join'
    members = request.form.get('members')
    group_id = request.form.get('group_id')

    print "- Token: %s" % token
    print "- Session: %s" % session
    print "- URL: %s" % url_join_group
    print "- Members: %s" % members
    print "- Group ID: %s" % group_id

    try:
        response = actions.join_group_test(token, session, url_join_group, group_id, members)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/group/remove', methods=['POST'])
def remove_member():
    print "Test API for remove member from groups..."
    token = eval(request.form.get('token'))
    session = request.form.get('session')
    url_remove_member = url + '/open/api/group/remove'
    members = request.form.get('members')
    group_id = request.form.get('group_id')

    print "- Token: %s" % token
    print "- Session: %s" % session
    print "- URL: %s" % url_remove_member
    print "- Members: %s" % members
    print "- Group ID: %s" % group_id

    try:
        response = actions.remove_group_member_test(token, session, url_remove_member, group_id, members)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message


@app.route('/api/group/exit', methods=['POST'])
def exit_group():
    print "Test API for exit groups..."
    token = eval(request.form.get('token'))
    session = request.form.get('session')
    url_exit_group = url + '/open/api/group/exit'
    group_id = request.form.get('group_id')

    print "- Token: %s" % token
    print "- Session: %s" % session
    print "- URL: %s" % url_exit_group
    print "- Group ID: %s" % group_id

    try:
        response = actions.exit_group_test(token, session, url_exit_group, group_id)
        return str(response)
    except Exception, e:
        print str(e)
        return api_error_message

if __name__ == '__main__':
    manager.run()
