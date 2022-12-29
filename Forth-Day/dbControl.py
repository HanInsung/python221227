import sqlite3 as db
import traceback
import sys
#from sqlite3 import *
# db.Connection.cursor()
# db.Connection.rollback()
# db.Connection.commit()
# db.Connection.close()
# db.Connection.execute()

try :
    #DB 접속(연결)객체 생성 및 Cursor 획득
    conn = db.connect('./sample.db')
    #conn = db.connect(':memory:') #memory db 접근
    cur = conn.cursor()

    # #테이블 생성
    # cur.execute("DROP TABLE IF EXISTS PhoneBook;")
    # print("------ Table Drop Complete!------ ")

    # cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
    # print("------ Table Create Complete!------ ")
    # #데이터 입력
    cur.execute("INSERT INTO PhoneBook Values('Derick', '010-1234-5678');")
    print("------ Insert Data Complete!------ ")

    #데이터 정의 입력
    name = 'SangJung'
    phoneNumber = '010-5670-2343'
    cur = conn.cursor()
    cur.execute('INSERT INTO PhoneBook VALUES(?, ?);', (name, phoneNumber))
    print("------ Insert Data Complete!------ ")

    name = 'SangJung'
    phoneNumber = '010-5670-2343'
    
    cur.execute('INSERT INTO PhoneBook VALUES(:name, :phoneNumber);', {"name":name, "phoneNumber":phoneNumber})
    conn.commit()

    print("------ Insert Data Complete!------ ")

    dataList = (('Tom', '010-543-5432'), ('DSP', '010-123-1234'))
    cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", dataList)
    print("------ Insert Data Complete!------ ")

    #데이터 출력
    cur.execute('SELECT * FROM PhoneBook')
    for row in cur:
        print(row)
    print("------ Select Data Complete!------ ")

    cur.execute('SELECT * FROM PhoneBook')
    cur.fetchall()
    #cur.fetchone()
    # cur.fetchmany(2)   
    print("------ Select Data Complete!------ ")

except db.Error as er:
    print('DB Error: %s' % (' '.join(er.args)))
    print("Exception class is :", er.__class__)
    print('DB traceback:')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))

else:
    print("-----DB processing complete!-----")

finally:
    conn.close()