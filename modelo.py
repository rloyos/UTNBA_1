import sqlite3 as sql

class Model:
    
    def createDB(self):
        conn = sql.connect("alumnos.db")
        conn.commit()
        conn.close()
    
    def createTable(self):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS alumnos (
            name text,
            last_name text,
            age integer,
            id integer
            )")
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


model = Model()
