from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
import requests
from . import signup,home
from flask_login import login_user,current_user
from control.client_mgmt import Client 
from db_model.mysql import conn_mysqldb




signin = Blueprint('signin', __name__,url_prefix='/home/signin')
# #사인업 폼 랜더
# @signin.route("/")
# def signinform(error=False):
#     return render_template('signin.html',error=error)

#사인업 폼 랜더
@signin.route("/")
def signinform(error=False):
    return render_template('signin.html',error=error)



#사인업 기능
@signin.route("/signincheck",methods=['POST'])
def signincheck():
    id1=request.form['id']
    password=request.form['password']
    check=Client.find(id1)
    #데이터 베이스에 저장된 아이디가 없고 함수가
    #불러진 위치가 singupform 이라면
    if check == True:
        error=id1
        return signup.signupform(error_log=error)


    #데이터 베이스에 저장돼어 있는 아이디가 있고 불러진 위치가 signupform 이라면
    #플라스크 로그인 세션에 id 값 저장 지금은 pno
    elif check != True:
        pw=Client.find_info(id1,'password')
        if pw == password:
            client=Client.get(id1)
            login_user(client)
            return home.index()
        else:
            return signup.signupform(error_log='password')
