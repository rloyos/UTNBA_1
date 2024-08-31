import sqlite3 as sql

class Connection:

    def __init__(self):
        self.base_datos = 'database/alumnos.db'
        self.conn = sql.connect(self.base_datos)
        self.cursor = self.conn.cursor()
        
    def closeDB(self):
        self.conn.commit()
        self.conn.close()