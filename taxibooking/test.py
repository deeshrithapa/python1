# from driver import Driver
# from searchdriver import searchDriver
# d1 = Driver()
# d1.setDID(1)
# searchDriver(d1)


import mysql.connector
import sys


def saveCustomer(customerInfo):
    conn = None
    sql = """INSERT INTO customers VALUES (%s, %s, %s, %s, %s)"""
    values = (customerInfo.getDID(),
              customerInfo.getName(),
              customerInfo.getAddress(),
              customerInfo.getEmail(),
              customerInfo.getPhonenumber())
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='final')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Data saved!")
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
