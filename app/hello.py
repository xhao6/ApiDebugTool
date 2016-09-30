# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required, DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
url = "https://cloudcn.v5.cn"
server = "http://192.168.1.171:5000"












if __name__ == '__main__':
    manager.run()
