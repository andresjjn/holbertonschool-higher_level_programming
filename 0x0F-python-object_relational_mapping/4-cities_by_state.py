#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def filter_cities_by_states():
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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM\
                   cities, states WHERE cities.state_id=states.id\
                   ORDER BY cities.id ASC""")
    records = cursor.fetchall()
    print(records)
    for state in records:
        print("{}".format(state))
    cursor.close()
    connection.close()
if __name__ == "__main__":
    filter_cities_by_states()
