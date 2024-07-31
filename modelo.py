import sqlite3 as sql

class Student:

    def __init__(self, name, last_name, age, id, phone, email, address, birth, creation_date):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.id = id
        self.phone = phone
        self.email = email
        self.address = address
        self.birth = birth
        self.creation_date = creation_date
    
    def createTable(self):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS alumnos (
            name text,
            last_name text,
            age integer,
            id integer
            )''')
        conn.commit()
        conn.close()

    def insertRow(self, name, last_name, age, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO alumnos VALUES ('{self.name}', '{self.last_name}', '{self.age}', '{self.id}')")
        conn.commit()
        conn.close()
    
    def rewriteRow(self, name, last_name, age, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE alumnos SET name = '{self.name}', last_name = '{self.last_name}', age = '{self.age}' WHERE id = '{self.id}'")
        conn.commit()
        conn.close()
    
    def deleteRow(self, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM alumnos WHERE id = '{self.id}'")
        conn.commit()
        conn.close()

    def orderedBy(self, arg):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM alumnos ORDER BY '{arg}'")
        conn.commit()
        conn.close()

    def showStudent(self, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM alumnos WHERE id = '{self.id}'")
        conn.commit()
        conn.close()

student = Student()
