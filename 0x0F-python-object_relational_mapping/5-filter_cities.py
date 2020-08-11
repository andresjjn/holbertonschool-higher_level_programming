#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def filter_all_cities_by_state():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    try:
        connection = MySQLdb.connect(host="localhost", port=3306,
                                     user=username, passwd=password,
                                     db=database)
    except:
        print("Can't connect to database")
        return
    cursor = connection.cursor()
    cursor.execute("""SELECT cities.name FROM cities LEFT JOIN states ON
                   cities.state_id=states.id WHERE states.name=(%s) ORDER BY
                   cities.id ASC""", (name, ))
    records = cursor.fetchall()
    lis = []
    if records is not None:
        for city in records:
            lis.append(city[0])
    print(", ".join(lis))
    cursor.close()
    connection.close()

if __name__ == "__main__":
    filter_all_cities_by_state()
