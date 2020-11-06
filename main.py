from flask import Flask, jsonify, request, render_template, make_response,redirect
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from view import home,signup,signin,logout,id_pw
from control.client_mgmt import Client
import os



# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static/')
CORS(app)
app.secure_key = os.urandom(50)

app.register_blueprint(home.home)
app.register_blueprint(signin.signin)
app.register_blueprint(signup.signup)
app.register_blueprint(logout.logout)
app.register_blueprint(id_pw.id_pw)

"""
로그인!!
"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'



#로그인 정보를 Client class 에서 객체로 가져오고, LoginManager() 에 추가하여 세션 생성
#current_user 객체에 해당 객체가 저장됨
#current_user.is_authenticated 호출시
@login_manager.user_loader
def load_user(client_id):
    return Client.get(client_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

#실행하면 바로 /home/으로 redirect
@app.route('/')
def index():
    return redirect('http://localhost:8080/home')



if __name__ == '__main__':
    #이게 있어야 플라스크에서 request를 기반으로 세션정보를 생성 할 수 있음
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    

    app.run(host='localhost', port='8080', debug=True)
