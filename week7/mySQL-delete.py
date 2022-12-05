# import
# connect with database
# delete record
# close connection
import sys  # to display error message
import mysql.connector  # to import CRUD
sql= """DELETE FROM persons WHERE pid=1"""
try:
    conn = mysql.connector.connect(host='localhost', username='root', password='', database='level4d')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("Delete records sucessfully.")
except:
    print("error", sys.exc_info())