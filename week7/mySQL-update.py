import sys
import mysql.connector
sql = """UPDATE persons set name='Yojana Gurung', address='Bagdole' WHERE pid=1"""
try:
    #connect
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')  # bridge

    #update
    cursor = conn.cursor()  # database
    cursor.execute(sql)
    conn.commit()

    #close
    cursor.close()
    conn.close()
    print("Update records sucessfully.")
except:
    print("error", sys.exc_info())