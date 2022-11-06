import sqlite3
import pandas as pd
import DBConnect as conn
from DBConnect import DBname

DB = conn.create_connection(DBname) 
c = DB.cursor()
                
def get_specific_data_from_table(variablenames, columnnames, tablename):
    query_string = "SELECT "
    for item in variablenames:
        query_string = query_string + item
    query_string = query_string + " FROM " + tablename
    c.execute(query_string)
    df = pd.DataFrame(c.fetchall(), columns=columnnames)
    return df


def get_all_data_from_table(table_name):
    query_string = "SELECT * FROM" + table_name
    c.execute(query_string)
    rows = c.fetchall()
    return rows