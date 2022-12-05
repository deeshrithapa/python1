import mysql.connector
import sys
# def insertRecords():
#     try:
#         sql = """INSERT INTO students VALUES(%s,%s,%s,%s)"""
#         values = [1, 'deeshri', 60, 80]
#         conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         conn.commit()  # save
#         cursor.close()
#         conn.close()
#         print("Records inserted.")
#     except:
#         print("error", sys.exc_info())


# def searchRecords():
#     try:
#         sid=(1,)
#         sql= """SELECT * FROM students WHERE sid=%s"""
#         conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor = conn.cursor()
#         cursor.execute(sql, sid)
#         record = cursor.fetchone()
#         print(record)
#         cursor.close()
#         conn.close()
#     except:
#         print("error", sys.exc_info())
def displayAll():
    try:
        sql="""SELECT * FROM students"""
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
        values=('aarya', 98, 77,1)
        sql = """ UPDATE students set name=%s, isd=%s, fcs=%s WHERE sid=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("records updated")
    except:
        print("error", sys.exc_info())
def deleteREcords():
    try:
        sid=(1,)
        sql = """DELETE FROM students WHERE sid=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql,sid)
        conn.commit()
        cursor.close()
        conn.close()
        print("record deleted")
    except:
        print("error", sys.exc_info())

# test
# insertRecords()
# searchRecords()
displayAll()
updateRecords()
deleteREcords()