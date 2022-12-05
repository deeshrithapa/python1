import mysql.connector
import sys

def saveDriver(driverInfo):
    conn = None
    sql= """INSERT INTO drivers VALUES %s, %s, %s, %s, %s, %s"""
    values = (driverInfo.getDID(),
              driverInfo.getName(),
              driverInfo.getAddress(),
              driverInfo.getEmail(),
              driverInfo.getPhoneNumbert(),
              driverInfo.getLicensePlate())
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='final')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("error", sys.exc_info())
    finally:
        del values
        del sql
        del conn
