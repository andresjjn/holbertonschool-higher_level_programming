#!/usr/bin/python3
import MySQLdb
import sys


def mysqlconnect():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        connection = MySQLdb.connect("localhost", username, password, database)
    except:
        print("Can't connect to database")
        return
    cursor = connection.cursor()
    cursor.execute("SELECT states.id, states.name FROM\
                   states ORDER BY states.id ASC")
    records = cursor.fetchall()
    for row in records:
        print("({}, '{}')".format(row[0], row[1]))
    cursor.close()
    connection.close()

mysqlconnect()
