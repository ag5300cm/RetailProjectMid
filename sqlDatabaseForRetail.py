
import sqlite3
from sqlite3 import Error


#  this should only run once, when you start up the program
def create_database_and_table():

    sqlite_file = "myDatabase.db"  # change database here
    table_name = "potatoTable"  # change table name here

    conn = sqlite3.connect(sqlite_file)  # making a connection
    c = conn.cursor()  # used for writing to the database

    # creating table here, can add more variables in the list if need be
    c.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(Purchaser Text,"
                                                           "Amount INTEGER)")

    conn.commit()  # Saving or changing the database with this command
    conn.close()  # closing connection

#
def save_search_data(Purchaser, Amount):

    sqlite_file = "myDatabase.db"  # change database here
    table_name = "potatoTable"  # change table name here

    conn = sqlite3.connect(sqlite_file)  # making a connection
    c = conn.cursor()  # used for writing to the database

    try:  # we will try and add the variables to the
        c.execute("INSERT INTO " + table_name + " (Purchaser, Amount)  VALUES(?,?)",
                  (Purchaser, Amount))
    except Error as e:
        print(e)

    conn.commit()  # Saving or changing the database with this command
    conn.close()  # closing connection

#
def get_saved_data(Purchaser):
    sqlite_file = "myDatabase.db"  # change database here
    table_name = "potatoTable"  # change table name here

    conn = sqlite3.connect(sqlite_file)  # making a connection
    c = conn.cursor()  # used for writing to the database

    try:  # we will try and add the variables to the
        c.execute('SELECT * FROM {tn} WHERE Purchaser= ? '. \
                  format(tn=table_name), (Purchaser,))
        alreadySearchedRow = c.fetchall()
        print(alreadySearchedRow)  # may delete
        for i in alreadySearchedRow:  # may delete
            print(i)
        return alreadySearchedRow  # returns the already searched info
    except Error as e:
        print(e)
    finally:
        conn.commit()  # Saving or changing the database with this command
        conn.close()  # closing connection

#
def select_all():
    sqlite_file = "myDatabase.db"  # change database here
    table_name = "potatoTable"  # change table name here

    conn = sqlite3.connect(sqlite_file)  # making a connection
    c = conn.cursor()  # used for writing to the database

    try:  # we will try and add the variables to the
        c.execute("SELECT * FROM " + table_name)
        alreadySearchedRow = c.fetchall()
        print(alreadySearchedRow)
    except Error as e:
        print(e)

    conn.commit()  # Saving or changing the database with this command
    conn.close()  # closing connection

def update_search_data(Purchaser, Amount):

    sqlite_file = "myDatabase.db"  # change database here
    table_name = "potatoTable"  # change table name here

    conn = sqlite3.connect(sqlite_file)  # making a connection
    c = conn.cursor()  # used for writing to the database

    try:  # we will try and add the variables to the
        c.execute("UPDATE INTO " + table_name + " (Purchaser, Amount)  VALUES(?,?)",
                  (Purchaser, Amount))
    except Error as e:
        print(e)

    conn.commit()  # Saving or changing the database with this command
    conn.close()  # closing connection


def delete_saved_data(Purchaser):
    sqlite_file = "myDatabase.db"  # change database here
    table_name = "potatoTable"  # change table name here

    conn = sqlite3.connect(sqlite_file)  # making a connection
    c = conn.cursor()  # used for writing to the database

    try:  # we will try and add the variables to the
        c.execute('DELETE FROM {tn} WHERE Purchaser= ? '. \
                  format(tn=table_name), (Purchaser,))
    except Error as e:
        print(e)
    finally:
        conn.commit()  # Saving or changing the database with this command
        conn.close()  # closing connection


#  just used for data testing, you should keep until everything is hooked up
#create_database_and_table()
#save_search_data("bbb", "asdfdsaf")  # for testing purposes now
#select_all()  # may delete
#search = "aaa"  # may delete
#previousInfo = get_saved_data(search) # may delete
#print(previousInfo)  # may delete
