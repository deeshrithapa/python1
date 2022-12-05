import sys

import mysql.connector


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
    except:
        print("error", sys.exc_info())
    finally:
        return conn

def insert(customer):
    conn = None
    sql = """INSERT INTO customers VALUES(%s, %s, %s, %s, %s)"""
    values = (customer.getCID(), customer.getName(), customer.getAddress(),customer.getEmail(), customer.getPhone())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("error", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result