from connection import Connection
from tkinter import messagebox

def createTable():
    connection = Connection()

    sql = '''
    CREATE TABLE alumnos(
    id INTEGER,
    name TEXT,
    last_name TEXT,
    age INTEGER,
    gender TEXT,
    creation INT)
'''
    try:
        connection.cursor.execute(sql)
        connection.closeDB()
        title = "Crear Registro"
        message = "Se creó la tabla en la base de datos."
        messagebox.showinfo(title, message)
    except:
        title = "Crear Registro"
        message = "La tabla ya está creada."
        messagebox.showwarning(title, message)

def deleteTable():
    connection = Connection()

    sql = "DROP TABLE alumnos"
    try:
        connection.cursor.execute(sql)
        connection.closeDB()
        title = "Borrar Registro"
        message = "Se borró la tabla en la base de datos."
        messagebox.showinfo(title, message)
    except:
        title = "Borrar Registro"
        message = "No hay tabla para borrar."
        messagebox.showerror(title, message)

    connection.cursor.execute(sql)
    connection.closeDB()

class Student:
    def __init__(self, id, name, last_name, age, gender, creation):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.creation = creation

    def __str__(self):
        return f"Alumno[{self.id}, {self.name}, {self.last_name}, {self.age}, {self.gender}, {self.creation}]"
    
def insert(student):
    connection = Connection()
    connection.cursor.execute(f"""INSERT INTO alumnos (id, name, last_name, age, gender, creation)
    VALUES ("{student.id}", "{student.name}", "{student.last_name}","{student.age}","{student.gender}", "{student.creation}")""")
    connection.closeDB()
    try:
        title = "Alumno agregado"
        message = "Se agregó al alumno con éxito."
        messagebox.showinfo(title, message)
    except:
        title = "Insertar Alumno"
        message = "La tabla 'Alumnos' no está creada en la base de datos. Por favor hacer click en 'Crear Base de Datos'."
        messagebox.showerror(title, message)

def list():
    connection = Connection()
    student_list = []
    sql = 'SELECT * FROM alumnos ORDER BY id DESC'

    try:
        connection.cursor.execute(sql)
        student_list = connection.cursor.fetchall()
        connection.closeDB()
    except:
        title = "Mostrar Alumnos"
        message = "Hubo un error."
        messagebox.showerror(title, message)

    return student_list

def edit(student, id):
    connection = Connection()
    sql = f"""UPDATE alumnos SET
           name = '{student.name}',
           last_name = '{student.last_name}',
           age = '{student.age}',
           gender = '{student.gender}',
           creation = '{student.creation}'
           WHERE id = {id}
           """
    try:
        connection.cursor.execute(sql)
        connection.closeDB()
    except:
        title = "Edición de Datos"
        message = "No se ha podido editar este registro."
        messagebox.showerror(title, message)

def delete(id):
    connection = Connection()
    sql = f"DELETE FROM alumnos WHERE id = {id}"

    try:
        connection.cursor.execute(sql)
        connection.closeDB()
    except:
        title = "Eliminación de Datos"
        message = "No se ha podido eliminar este registro."
        messagebox.showerror(title, message)