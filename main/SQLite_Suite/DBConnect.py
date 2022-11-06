import sqlite3

DBname = 'hacksqlite.db'

def create_connection(db_file):
    return sqlite3.connect(db_file)
    