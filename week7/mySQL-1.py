# install library to connect
# https://pypi.org/
# pip install mysql-connector-python

# connect with database server
# import library
import mysql.connector
import sys
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='level4d'
    )  # connect with mysql server
    conn.close()  # connection close
    print("connect with database server sucessfully")
except:
    print("error", sys.exc_info())


