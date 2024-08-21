import sqlite3 as sql
import os

BASE_DATOS = 'alumnos.db'
TABLA = 'alumnos'

class Student:

    def __init__(self, name, last_name, age, id, birth, creation_date):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.id = id
        self.birth = birth
        self.creation_date = creation_date

# Creates/Connect table if not created/connected before.

    def createDB(var: str) -> sql.Connection:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(base_dir, var)

        return sql.connect(base_path)
    
    
    def createTable(self):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {TABLA} (
            name TEXT,
            last_name TEXT,
            age INTEGER,
            id INTEGER
            )''')
        conn.commit()

    def insertStudent(self, name, last_name, age, id):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {TABLA} VALUES ('{self.name}', '{self.last_name}', '{self.age}', '{self.id}')")
        conn.commit()
    
    def rewriteStudent(self, name, last_name, age, id):
        conn = sql.connect(BASE_DATOS)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {TABLA} SET name = '{self.name}', last_name = '{self.last_name}', age = '{self.age}' WHERE id = '{self.id}'")
        conn.commit()
    
    def deleteStudent(self, id):
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

student = Student("name", "last_name", "age", "id", "creation_date")
