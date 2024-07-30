import sqlite3 as sql

class Model:
    
    def createDB(self):
        conn = sql.connect("alumnos.db")
        conn.commit()
        conn.close()
    
    def createTable(self):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        instruction = f"CREATE TABLE IF NOT EXISTS alumnos (
            name text,
            last_name text,
            age integer,
            id integer
            )"
        cursor.execute(instruction)
        conn.commit()
        conn.close()

    def insertRow(self, name, last_name, age, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        instruction = f"INSERT INTO alumnos VALUES ('{name}', '{last_name}', '{age}', '{id}')"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
        
    #No estoy para nada seguro de este método:
    
    def rewriteRow(self, name, last_name, age, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        instruction = f"UPDATE alumnos SET name = {name} last_name = {last_name} age = {age} id = {id}"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
    
    def deleteRow(self, id):
        conn = sql.connect("alumnos.db")
        cursor = conn.cursor()
        instruction = f"DELETE FROM alumnos WHERE id = '{id}'"
        cursor.execute(instruction)
        conn.commit()
        conn.close()

    def ordered(self):
        conn = sql.connext("alumnos.db")
        cursor = conn.cursor()
        instruction = f"SELECT * FROM alumnos ORDER BY name"
        cursor.execute(instruction)
        conn.commit()
        conn.close()

model = Model()
