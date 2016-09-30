from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import *
import requests

server = "http://192.168.1.171:5000"


@main.route('/opendoc', methods=['GET', 'POST'])
def opendoc():
    return render_template('opendoc.html')


@main.route('/', methods=['GET', 'POST'])
def index():
    data = ""

    category_form = CategoryForm()
    if category_form.validate_on_submit():
        if category_form.api_name.data == 'get_token':
            return redirect(url_for('main.param_get_token'))
        if category_form.api_name.data == 'create_user':
            return redirect(url_for('main.param_create_user'))
        if category_form.api_name.data == 'update_session':
            return redirect(url_for('main.param_update_session'))
        if category_form.api_name.data == 'update_nickname':
            return redirect(url_for('main.param_update_nickname'))
        if category_form.api_name.data == 'create_group':
            return redirect(url_for('main.param_create_group'))
        if category_form.api_name.data == 'update_group':
            return redirect(url_for('main.param_update_group'))
        if category_form.api_name.data == 'group_info':
            return redirect(url_for('main.param_get_group_info'))
        if category_form.api_name.data == 'join_group':
            return redirect(url_for('main.param_join_group'))
        if category_form.api_name.data == 'remove_user_from_group':
            return redirect(url_for('main.param_remove_member_from_group'))
        if category_form.api_name.data == 'exit_group':
            return redirect(url_for('main.param_exit_group'))
    return render_template('index.html', form=category_form, data = data)


@main.route('/param/token', methods=['GET', 'POST'])
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


@main.route('/param/create_user', methods=['GET', 'POST'])
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


@main.route('/param/update_session', methods=['GET', 'POST'])
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


@main.route('/param/update_nickname', methods=['GET', 'POST'])
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


@main.route('/param/create_group', methods=['GET', 'POST'])
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


@main.route('/param/update_group', methods=['GET', 'POST'])
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


@main.route('/param/get_group_info', methods=['GET', 'POST'])
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


@main.route('/param/join_group', methods=['GET', 'POST'])
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


@main.route('/param/remove_member', methods=['GET', 'POST'])
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


@main.route('/param/exit_group', methods=['GET', 'POST'])
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