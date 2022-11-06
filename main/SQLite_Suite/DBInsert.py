import sqlite3
import DBConnect as conn
from DBConnect import DBname
import pandas as pd

DB = conn.create_connection(DBname)
c = DB.cursor()

def insert_into_table(tablename, columnnames, values):
    query_string = "INSERT INTO " + tablename + "("
    for column in columnnames:
        query_string = query_string + column + ","
    query_string = ") VALUES "
    for dual in values:
        query_string = query_string + "(" + dual + "),"
    
    c.execute(query_string)
    c.execute('''
          INSERT INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150)
          ''')
    DB.commit()