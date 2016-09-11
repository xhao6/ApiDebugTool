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
    api_name = SelectField(u'Step.1 选择调试接口：</br ></br >', choices=[('get_token', u'OAuth2 Token 获取'), ('create_user', u'创建用户'),
                ('update_session', u'刷新用户 SessionID'),('update_nickname', u'更新用户信息'), ('create_group', u'创建群组'),
                ('update_group', u'更新群组'), ('group_info', u'获取群组信息'), ('join_group', u'加入群组'),
                ('remove_user_from_group', u'将用户从群组中移除'), ('exit_group', u'解散或退出群组')])
    submit = SubmitField(u'下一步')


class ParameterGetTokenForm(Form):
    app_id = StringField(u'Step.2 输入API参数：</br ></br >appid:', validators=[Required()])
    secret = StringField('secret:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterCreateUserForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    app_user_id = StringField('app_user_id:', validators=[Required()])
    nickname = StringField('nickname:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterUpdateSessionForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    app_user_id = StringField('app_user_id:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterUpdateNickname(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    app_user_id = StringField('app_user_id:', validators=[Required()])
    nickname = StringField('nickname:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterCreateGroupForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    members = StringField('members:', validators=[Required()])
    group_name = StringField('group_name:', validators=[Required()])
    group_description = StringField('group_description:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterUpdateGroupForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    group_id = StringField('group_id:', validators=[Required()])
    group_name = StringField('group_name:', validators=[Required()])
    group_description = StringField('group_description:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterGetGroupInfoForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    group_id = StringField('group_id:', validators=[Required()])
    detail = StringField('detail:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterJoinGroupInfoForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    group_id = StringField('group_id:', validators=[Required()])
    members = StringField('members:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterRemoveMemberFromGroupForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    group_id = StringField('group_id:', validators=[Required()])
    members = StringField('members:', validators=[Required()])
    submit = SubmitField(u'测试')


class ParameterExitGroupForm(Form):
    token = StringField(u'Step.2 输入API参数：</br ></br >token:', validators=[Required()])
    session = StringField('session:', validators=[Required()])
    group_id = StringField('group_id:', validators=[Required()])
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

    category_form = CategoryForm()
    if category_form.validate_on_submit():
        if category_form.api_name.data == 'get_token':
            return redirect(url_for('param_get_token'))
        if category_form.api_name.data == 'create_user':
            return redirect(url_for('param_create_user'))
        if category_form.api_name.data == 'update_session':
            return redirect(url_for('param_update_session'))
        if category_form.api_name.data == 'update_nickname':
            return redirect(url_for('param_update_nickname'))
        if category_form.api_name.data == 'create_group':
            return redirect(url_for('param_create_group'))
        if category_form.api_name.data == 'update_group':
            return redirect(url_for('param_update_group'))
        if category_form.api_name.data == 'group_info':
            return redirect(url_for('param_get_group_info'))
        if category_form.api_name.data == 'join_group':
            return redirect(url_for('param_join_group'))
        if category_form.api_name.data == 'remove_user_from_group':
            return redirect(url_for('param_remove_member_from_group'))
        if category_form.api_name.data == 'exit_group':
            return redirect(url_for('param_exit_group'))
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
    return render_template('step2.html', form = form, response = response)


@app.route('/param/create_user', methods=['GET', 'POST'])
def param_create_user():
    response = ''
    form = ParameterCreateUserForm()
    if form.validate_on_submit():
        token = form.token.data
        app_user_id = form.app_user_id.data
        nickname = form.nickname.data
        data = {"token": token, "app_user_id": app_user_id, "nickname": nickname}
        request_url = server + '/api/user/create'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/update_session', methods=['GET', 'POST'])
def param_update_session():
    response = ''
    form = ParameterUpdateSessionForm()
    if form.validate_on_submit():
        token = form.token.data
        app_user_id = form.app_user_id.data
        data = {"token": token, "app_user_id": app_user_id}
        request_url = server + '/api/user/session'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/update_nickname', methods=['GET', 'POST'])
def param_update_nickname():
    response = ''
    form = ParameterUpdateNickname()
    if form.validate_on_submit():
        token = form.token.data
        app_user_id = form.app_user_id.data
        nickname = form.nickname.data
        session = form.session.data
        data = {"token": token, "app_user_id": app_user_id, "nickname": nickname, "session": session}
        request_url = server + '/api/user/nickname'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/create_group', methods=['GET', 'POST'])
def param_create_group():
    response = ''
    form = ParameterCreateGroupForm()
    if form.validate_on_submit():
        token = form.token.data
        session = form.session.data
        members = form.session.data
        group_name = form.group_name.data
        group_description = form.group_description.data
        data = {"token": token, "session": session, "members": members, "group_name": group_name, "group_description": group_description}
        request_url = server + '/api/group/create'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/update_group', methods=['GET', 'POST'])
def param_update_group():
    response = ''
    form = ParameterUpdateGroupForm()
    if form.validate_on_submit():
        token = form.token.data
        session = form.session.data
        group_id = form.group_id.data
        group_name = form.group_name.data
        group_description = form.group_description.data
        data = {"token": token, "session": session, "group_id": group_id, "group_name": group_name, "group_description": group_description}
        request_url = server + '/api/group/update'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/get_group_info', methods=['GET', 'POST'])
def param_get_group_info():
    response = ''
    form = ParameterGetGroupInfoForm()
    if form.validate_on_submit():
        token = form.token.data
        session = form.session.data
        group_id = form.group_id.data
        detail = form.detail.data
        data = {"token": token, "session": session, "group_id": group_id, "detail": detail}
        request_url = server + '/api/group/get'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/join_group', methods=['GET', 'POST'])
def param_join_group():
    response = ''
    form = ParameterJoinGroupInfoForm()
    if form.validate_on_submit():
        token = form.token.data
        session = form.session.data
        group_id = form.group_id.data
        members = form.members.data
        data = {"token": token, "session": session, "group_id": group_id, "members": members}
        request_url = server + '/api/group/join'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/remove_member', methods=['GET', 'POST'])
def param_remove_member_from_group():
    response = ''
    form = ParameterJoinGroupInfoForm()
    if form.validate_on_submit():
        token = form.token.data
        session = form.session.data
        group_id = form.group_id.data
        members = form.members.data
        data = {"token": token, "session": session, "group_id": group_id, "members": members}
        request_url = server + '/api/group/remove'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


@app.route('/param/exit_group', methods=['GET', 'POST'])
def param_exit_group():
    response = ''
    form = ParameterExitGroupForm()
    if form.validate_on_submit():
        token = form.token.data
        session = form.session.data
        group_id = form.group_id.data
        data = {"token": token, "session": session, "group_id": group_id}
        request_url = server + '/api/group/exit'
        print "- %r" % request_url
        response = requests.post(request_url, data=data).text
    return render_template('step2.html', form=form, response=response)


if __name__ == '__main__':
    manager.run()
