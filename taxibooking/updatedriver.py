import sys
import mysql.connector
def updateDriver():
    try:
        values=('aarya', 9899 ,1)
        sql = """ UPDATE drivers set name=%s, licenseno=%s WHERE did=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("records updated")
    except:
        print("error", sys.exc_info())