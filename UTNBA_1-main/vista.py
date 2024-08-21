import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Listbox
from tkinter import messagebox
import sqlite3 as sql

from modelo import Student
from modelo import BASE_DATOS
from modelo import TABLA

class Vista:
    def vista_principal(self, root):
        self.root = root
        root = Tk()
        root.geometry('600x500')
        root.resizable(True, True)
        root.title("Gestión de Alumnos")

        variables_list = [Student.insertStudent, Student.rewriteStudent, Student.deleteStudent, Student.orderedByABC, Student.showStudent]
        
        #Config general
        style = ttk.Style()
        style.configure("alto_fila.Treeview", rowheight=40)
        Label(root, text="", width=10, height=1).grid(row=8, column=0)

        #Configuración de la vista // Nombre

        self.name_label = Label(root, text = "Nombre: ")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        #Configuración de la vista // Apellido
        
        self.last_name_label = Label(root, text = "Apellido: ")
        self.last_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.last_name_entry = Entry(root)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)

        #Configuración de la vista // Edad
        
        self.age_label = Label(root, text = "Edad: ")
        self.age_label.grid(row=2, column=0, padx=10, pady=10)
        self.age_entry = Entry(root)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        #Configuración de la vista // DNI
        
        self.id_label = Label(root, text = "DNI: ")
        self.id_label.grid(row=3, column=0, padx=10, pady=10)
        self.id_entry = Entry(root)
        self.id_entry.grid(row=3, column=1, padx=10, pady=10)

        #Creación de ficha // Creación

        self.creation_label = Label(root, text = "Creación de ficha: ")
        self.creation_label.grid(row=4, column=0, padx=10, pady=10)
        self.creation_entry = Entry(root)
        self.creation_entry.grid(row=4, column=1, padx=10, pady=10)

        #Botón AGREGAR ALUMNO

        self.insert_button = Button(root, text="Agregar Alumno", command=lambda: (Student.insertStudent(f"{self.name}, {self.last_name}, {self.age}, {self.id}, {self.creation_date}")))
        self.insert_button.grid(row=5, column=0, padx=10, pady=10)

        #Botón EDITAR ALUMNO

        self.rewrite_button = Button(root, text="Editar Alumno", command=lambda: (Student.rewriteStudent(root, variables_list, BASE_DATOS, TABLA), ))
        self.rewrite_button.grid(row=5, column=1, padx=10, pady=10)

        #Botón ELIMINAR ALUMNO

        self.delete_button = Button(root, text="Eliminar Alumno", command=lambda: (Student.deleteStudent(root, variables_list, BASE_DATOS, TABLA), ))
        self.delete_button.grid(row=5, column=2, padx=10, pady=10)

        #Botón MOSTRAR ALUMNO

        self.show_button = Button(root, text="Mostrar Alumnos", command=lambda: (Student.showStudent(root, variables_list, BASE_DATOS, TABLA), ))
        self.show_button.grid(row=5, column=3, padx=20, pady=10)

        #Ejecutar

        self.Students_list = Listbox(root)
        self.Students_list.grid(row=6, column=1, padx=0, pady=0)

        root.mainloop()


vista = Vista()