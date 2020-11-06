from db_model.mysql import conn_mysqldb
mysql_db = conn_mysqldb()
db_cursor = mysql_db.cursor()

sql ='select * from client'
db_cursor.execute(sql)
user = db_cursor.fetchone()
print("----------------------------------------------")
print(user)
print("----------------------------------------------")


sql ='select * from client'
db_cursor.execute(sql)
user = db_cursor.fetchall()
print("----------------------------------------------")
print(user)
print("----------------------------------------------")