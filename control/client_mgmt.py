from flask_login import UserMixin
from db_model.mysql import conn_mysqldb

class Client(UserMixin): 
    def __init__(self, user_pno):
        self.id = user_pno#self.id 이건 국룰이야 !!

    def get_id(self):
        return str(self.id)

    #유저가 존재 하는지 안하는제 췤
    @staticmethod
    def find(client_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "select * from client where pno='{}'".format(client_id)
        # print (sql)
        db_cursor.execute(sql)
        check = db_cursor.fetchone()
        mysql_db.close()
        db_cursor.close()
        #유저가 데이터 베이스에 없다면..
        if not check:
            #리턴을 참으로
            return True
        #유저가 데이터베이스에 없다면 리턴을 userid 이경우에는 pno 겠징
        return client_id

    #유저 정보 하나만 찾을때
    @staticmethod
    def find_info(client_id,column):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "select {} from client where pno='{}'".format(column,client_id)
        db_cursor.execute(sql)
        info = db_cursor.fetchone()
        mysql_db.close()
        db_cursor.close()
        print(info)
        #유저가 데이터 베이스에 없다면..
        if not info:
            #리턴을 거짓으로
            return False

        #유저가 데이터베이스에 있으면 리턴
        return info[0]




    #로그인 기능 구현 을 위한 함수 
    #로그인 기능 호출시 유저 객체를 생성한ㄷ.
    @staticmethod
    def get(client_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "select * from client where pno='{}'".format(client_id)
        # print (sql)
        db_cursor.execute(sql)
        check= db_cursor.fetchone()

        mysql_db.close()
        db_cursor.close()
        #유저가 데이터 베이스에 없다면..
        if not check:
             #리턴을 거짓으로
            return False

        #있으면 클라이언트 객체 생성 후 객체를 리턴
        client=Client(client_id)
        return client

        

#클라이언트 생성
    @staticmethod
    def create(**kwargs):
        client=Client.find(kwargs["pno"])
        #클라이언트가 db에 없으면
        if client == True:
            sql="insert into client values('{pno}','{lname}{fname}','{sex}', '{password}', '{nation}','{birthday}','{Issue}','{Expiry}',0);".format(pno=kwargs['pno'],lname=kwargs['lname'],fname=kwargs['fname'],sex=kwargs['sex'],password=kwargs['password'],nation=kwargs['nation'],birthday=kwargs['birthday'],Issue=kwargs['Issue'],Expiry=kwargs['Expiry'])
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            db_cursor.execute(sql) 
            mysql_db.commit()
            mysql_db.close()
            db_cursor.close()
            return True
        else:
            return client


