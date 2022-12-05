# import
import sys
import mysql.connector
sql="""INSERT INTO persons VALUES(1, 'Deeshri Thapa', 'Jhamsikhel')"""
try:
    #connect
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="level4d")
    #insert
    cursor=conn.cursor()  # traveller
    cursor.execute(sql)  # insert
    conn.commit()  # save
    #close
    cursor.close()
    conn.close()
    print("insert record sucessfully")
except:
    print("error", sys.exc_info())  # display error message
