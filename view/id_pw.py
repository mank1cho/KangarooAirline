from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
import requests
from . import signup,home
from flask_login import login_user,current_user
from control.client_mgmt import Client 
from db_model.mysql import conn_mysqldb




id_pw = Blueprint('id_pw', __name__,url_prefix='/home/id_pw')
# #사인업 폼 랜더
# @signin.route("/")
# def signinform(error=False):
#     return render_template('signin.html',error=error)

#사인업 폼 랜더
@id_pw.route("/")
def idpwform(error=False):
    return render_template('id_password.html')
