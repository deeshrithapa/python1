import mysql.connector
import sys
from driver import Driver

def displayAll():

    try:
        sql = """SELECT * FROM drivers"""

        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
    except:
        print("error", sys.exc_info())
