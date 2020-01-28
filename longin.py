'''模拟注册和登录'''

import pymysql

db= pymysql.connect(host = 'localhost',
                   port =3306,
                   user ='root',
                   password = '123456',
                   database = 'stu',
                   charset ='utf8')

cur = db.cursor()



#注册
def register():
    username = input('username:')
    password = input('password:')
    sql="select * from login where username='%s'" %username
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return False

    try:
        sql='insert into login (username,password) values (%s,%s)'
        cur.execute(sql,[username,password])
        db.commit()
        return True

    except:
        db.rollback
        return False

def login():
    username=input('username:')
    password=input('password:')
    sql= "select * from login where username='%s'" \
         " and password='%s'" %(username,password)
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return True

while True:
    print("""
    ===============
    1.注册    2.登录
    ===============
    """)
    cmd=input('输入命令：')
    if cmd=='1':
        if register():
            print('注册成功')
        else:
            print("注册失败")
    elif cmd=='2':
        if login():
            print('登录成功')
            break
        else:
            print('登录失败')

cur.close()
db.close()


