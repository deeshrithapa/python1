import sys
import mysql.connector
def deleteDriver():
    try:
        did = (1,)
        sql = """DELETE FROM drivers WHERE did=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, did)
        conn.commit()
        cursor.close()
        conn.close()
        print("record deleted")
    except:
        print("error", sys.exc_info())



