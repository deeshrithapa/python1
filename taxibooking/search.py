import sys

import mysql.connector


# def searchDriver(ln):
#     conn = None
#     sql = """SELECT * FROM drivers WHERE licenseno=%s"""
#     values = (ln,)
#     driver = None
#     try:
#         conn = mysql.connector.Connect(host='localhost', user='root', password='', database='level4d')
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         driver = cursor.fetchall()
#         cursor.close()
#         conn.close()
#     except:
#         print("error:", sys.exc_info())
#     finally:
#         del values
#         del sql
#         del conn
#         return driver
*
def editDriver(driverInfo):
    conn = None
    sql = """UPDATE drivers SET name=%s, licenseno=%s WHERE did=%s"""
    values = (driverInfo.getName(), driverInfo.getLicenseNo(), driverInfo.getDID())
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True

    except:
        print("error:", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

# def deleteDriver(did):
#     conn = None
#     sql = """DELETE FROM drivers WHERE did=%s"""
#     values = (did,)
#     result = False
#     try:
#         conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         result = True

#
#
#     except:
#         print("error:", sys.exc_info())
#     finally:
#         del values
#         del sql
#         del conn
#         return result

# def allDriver():
#     conn = None
#     sql = """ SELECT * FROM drivers"""
#     drivers = None
#
#     try:
#         conn = mysql.connector.Connect(host='localhost', user='root', password='', database='level4d')
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         drivers = cursor.fetchall()
#         cursor.close()
#         conn.close()
#     except:
#         print("error:", sys.exc_info())
#     finally:
#         del sql
#         del conn
#         return drivers



