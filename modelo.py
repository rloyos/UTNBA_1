import sqlite3 as sql


def createDB():
    conn = sql.connect("alumnos.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE alumnos (
        name text,
        last_name text,
        age integer,
        id integer
        )"""
    )
    conn.commit()
    conn.close()
    
def insertRow(name, last_name, age, id):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO alumnos VALUES ('{name}', '{last_name}', '{age}', '{id}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def deleteRow(id):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM alumnos WHERE id = '{id}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    pass