
import pymysql

db= pymysql.connect(host = 'localhost',
                   port =3306,
                   user ='root',
                   password = '123456',
                   database = 'stu',
                   charset ='utf8')

cur = db.cursor()

# with open('image.jpg','rb') as f:
#     data=f.read()
#
#
# try:
#     sql="update class set image=%s where name ='Jame'"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

#获取图片
sql='select image from class where name="Jame"'
cur.execute(sql)
data =cur.fetchone()
with open('girl.jpg','wb') as f:
    f.write(data[0])

cur.close()
db.close()