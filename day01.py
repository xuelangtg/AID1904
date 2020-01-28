'''dict'''

import pymysql
import re

ft= open('dict.txt')

#建立链接
db= pymysql.connect(host = 'localhost',
                   port =3306,
                   user ='root',
                   password = '123456',
                   database = 'word',
                   charset ='utf8')

cur = db.cursor()

sql="insert into dict (word,mean) values (%s,%s)"

for line in ft:
    tem=re.findall(r'(\S+)\s+(.*)',line)[0]
    try:
        cur.execute(sql,tem)
        db.commit()

    except:
        db.rollback()

ft.close()

cur.close()
db.close()








