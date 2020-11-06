from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
import requests
from db_model.mysql import conn_mysqldb
from flask_login import login_user, current_user, logout_user

home = Blueprint('home', __name__,url_prefix='/home')

#홈화면 랜더
@home.route("/")
def index():
    if current_user.is_authenticated:            
        return render_template('/index.html',login=True)
    else:
        return render_template('/index.html',login=False)


"""
로그인
로그아웃을
홈에 추가해야 할지 아니면 다른 py 로 만드는게 맞는지 모르것냉;;
"""