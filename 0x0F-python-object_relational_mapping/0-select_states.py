#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def mysqlconnect():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password,
                                     db=database)
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
if __name__ == "__main__":
    mysqlconnect()
