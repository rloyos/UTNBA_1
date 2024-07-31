import sqlite3
import os

BASE_DATOS = 'alumnos.db'
TABLA = 'alumnos'

def createDB():
    base_directory = os.path.dirname(os.path.abspath(_file_))
    base_path = os.path.join(base_directory, BASE_DATOS)
    conection = sql.connect(base_path)
    return conection
