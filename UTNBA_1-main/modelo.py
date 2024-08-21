import sqlite3 as sql
import os

BASE_DATOS = 'alumno.db'
TABLA = 'alumnos'

class Student:

    def __init__(self,):
        pass
        '''self.name = name
        self.last_name = last_name
        self.age = age
        self.id = id
        self.gender = gender 
        '''

# Creates/Connect table if not created/connected before.

    '''def createDB(var: str) -> sql.Connection:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(base_dir, var)

        return sql.connect(base_path)'''
    
    def createDB(self):
        conn = sql.connect(BASE_DATOS)
        conn.commit()
        conn.close()
    
    
    def createTable(self):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {TABLA} (
            name TEXT,
            last_name TEXT,
            age INTEGER,
            id INTEGER PRIMARY KEY,
            gender TEXT
            )""")
        conn.commit()
        conn.close

    def insertStudent(self, name):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        query = (f"INSERT INTO {TABLA} ({self.name}) VALUES (?)")
        data_insert = (name)
        cursor.execute(query, data_insert)
        conn.commit()
        conn.close()
    
    def rewriteStudent(self, name, last_name, age, id, gender):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {TABLA} SET name = '{self.name}', last_name = '{self.last_name}', age = '{self.age}' WHERE id = '{self.id}'")
        conn.commit()
    
    def deleteStudent(self, id):
        self.id = id
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABLA} WHERE id = '{self.id}'")
        conn.commit()

    def orderedByABC(self):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLA} ORDER BY {self.last_name} DESC")
        conn.commit()

    def showStudent(self, id):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLA} WHERE id = '{id}'")
        conn.commit()

student = Student()

student.createDB()
student.createTable()
