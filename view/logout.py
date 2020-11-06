from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
import requests
from . import signup,home
from flask_login import logout_user,current_user
from control.client_mgmt import Client 
from db_model.mysql import conn_mysqldb


logout = Blueprint('logout', __name__,url_prefix='/home/logout')


@logout.route('/')
def logoutform():
    logout_user()
    return redirect(url_for('home.index'))