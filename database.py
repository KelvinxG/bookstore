

import sqlite3


#establish a connection to sqlite
conn=sqlite3.connect("bookstore.db")


#create a TABLE for bookstore
conn.execute('''
             CREATE TABLE Bookstore(
             	uuid INTEGER PRIMARY KEY,
                book_name TEXT NOT NULL,
                author_name TEXT NOT NULL,
                description TEXT NOT NULL,
                year_release INTEGER
             )          
             ''')