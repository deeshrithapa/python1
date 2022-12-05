import mysql.connector
import sys
def insertRecords():
    try:
        sql = """INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s)"""
        values = [1, 'Deeshri Thapa', 'Jhamsikhel', 'deeshri@gmail.com','deeshri','+9779813415277']
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()  # save
        cursor.close()
        conn.close()
        print("Records inserted.")
    except:
        print("error", sys.exc_info())

def searchRecords():
    try:
        email=('deeshri@gamil.com',)
        sql= """SELECT * FROM users WHERE email=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, email)
        record = cursor.fetchone()
        print(record)
        cursor.close()
        conn.close()
    except:
        print("error", sys.exc_info())

def displayAll():
    try:
        sql = """SELECT * FROM users"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
    except:
        print("error", sys.exc_info())

def updateRecords():
    try:
        values = ('aarya yadav','biratnagar','+9779851011989', '1','password', 'deeshri@gmail.com')
        sql = """ UPDATE users set fullname=%s, address=%s, mobile=%s,uid=%s, password=%s WHERE email=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("records updated")
    except:
        print("error", sys.exc_info())

def deleteRecords():
    try:
        email= ('deeshri@gmail.com',)
        sql = """DELETE FROM users WHERE email=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, email)
        conn.commit()
        cursor.close()
        conn.close()
        print("record deleted")
    except:
        print("error", sys.exc_info())

insertRecords()
searchRecords()
displayAll()
updateRecords()
deleteRecords()
