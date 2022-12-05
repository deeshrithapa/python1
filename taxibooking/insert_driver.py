import mysql.connector
import sys


def saveDriver(driverInfo):
    conn = None
    sql = """INSERT INTO drivers VALUES (%s, %s, %s)"""
    values = (driverInfo.getDID(),
              driverInfo.getName(),
              driverInfo.getLicenseNo())
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Save Driver!")
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

# def searchDriver(licenseno):
#     pass
def updateDriver(driverInfo):
    pass
def deleteDriver(did):
    pass
def allDrivers():
    pass