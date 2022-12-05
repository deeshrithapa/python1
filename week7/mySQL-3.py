import mysql.connector
import sys

def insertRecord(userInfo):
    conn= None
    sql = """INSERT INTO users values(%s, %s, %s, %s, %s, %s)"""
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port='3306',database='level4d')
        cursor= conn.cursor()
        cursor.execute(sql, userInfo)
        conn.commit()
        cursor.close()
        conn.close()
        print("User inserted.")

    except:
        print("error", sys.exc_info())
    finally:
        del conn
        del sql

def loginUser(userInfo):
    conn = None
    sql = """SELECT * FROM users WHERE email=%s and password=%s"""
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, userInfo)
        user = cursor.fetchall()
        print(user)
        if user!= None:
            print('Welcome', user[0][1])
        else:
            print('User not found.')
        cursor.close()
        conn.close()



    except:
        print("error", sys.exc_info())
    finally:
        del sql
        del conn




# test
# userInfo = (1, 'Aarya Yadav', 'biratnagar', 'aarya@gmail.com', '9851011988', '1234',)
# insertRecord(userInfo)

userInfo = ('aarya@gmail.com', '1234')
loginUser(userInfo)

