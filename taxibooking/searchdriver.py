import mysql.connector
import sys
from driver import Driver


def searchDriver(driverInfo):


    try:
        did =(1,)
        sql = """ SELECT * FROM drivers WHERE did=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, did)
        record = cursor.fetchone()
        print(record)
        cursor.close()
        conn.close()
        print("Search Driver!")

    except:
        print("Error : ", sys.exc_info())



