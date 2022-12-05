import sys
import mysql.connector
sql=""" SELECT * FROM persons """  # where pid=1 if needed to select a specific records
try:
    conn= mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    conn.close()
    print("Record retrieved sucessfully.")
except:
    print("error", sys.exc_info())
