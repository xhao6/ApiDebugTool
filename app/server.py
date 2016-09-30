# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager

from lib import actions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
url = "https://cloudcn.v5.cn"
api_error_message = u"输入错误，请检查接口参数"


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
        response = actions.update_nickname_test(token, session, url_update_user, app_user_id, app_user_nick_name)
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
