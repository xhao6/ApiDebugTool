# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, DataRequired


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