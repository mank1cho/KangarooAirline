from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
import requests
from control.client_mgmt import Client 
from db_model.mysql import conn_mysqldb


signup = Blueprint('signup', __name__,url_prefix='/home/signup')

"""
사인업 기능
"""
#사인업 폼 렌더
@signup.route("/signupform")
def signupform(error=False,error_log=False,**kwargs):
    #kwargs에 값이 없으면 그냥 호출
    if not kwargs:            
        return render_template('/signup.html',error=error,error_log=error_log)
    else:
        return render_template('/signup.html',error=error,error_log=error_log,kwargs=kwargs)


#사인업 체크 control.client_mgmt에서 리턴 받은 값을 전해주는게 맞나??? ㅅㅂ
@signup.route("/signupcheck",methods=['POST'])
def signupcheck():
    args_dict = request.form.to_dict()
    check = Client.create(**args_dict)
    if check ==True:
        return signupcomplete(request.form['pno'],request.form['fname'],request.form['lname'],request.form['nation'],request.form['birthday'])
    else:
        return signupform(error=check,**args_dict)

#사인업 실패시..
@signup.route("/signupcomplete")
def signupcomplete(*args,error=False):
    data=[]
    for i in args:
        data.append(i)
    return render_template('signup_complete.html',data=data,error=error)




"""
로그인 함수
"""
