import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import Frame
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Listbox
from tkinter import Spinbox
from tkinter import LabelFrame
from tkinter import Checkbutton
from tkinter import IntVar
from tkinter import messagebox
import sqlite3 as sql

from modelo import Student
from modelo import BASE_DATOS
from modelo import TABLA

class Vista:
    def vista_principal(self, window):
        self.window = window
        window = Tk()
        frame = Frame(window)
        frame.pack()
        window.title("Gestión de Alumnos")

        variables_list = [Student.insertStudent, Student.rewriteStudent, Student.deleteStudent, Student.orderedByABC, Student.showStudent]

        #User Information
        user_info = LabelFrame(frame, text="Completar:")
        user_info.grid(row= 0, column= 0, padx=20, pady=20)

        #Configuración de la vista // Nombre
        name_label = Label(user_info, text = "Nombre: ")
        name_label.grid(row=1, column=0)
        name_entry = Entry(user_info)
        name_entry.grid(row=1, column=1)

        #Configuración de la vista // Apellido
        
        last_name_label = Label(user_info, text = "Apellido: ")
        last_name_label.grid(row=2, column=0)
        last_name_entry = Entry(user_info)
        last_name_entry.grid(row=2, column=1)

        #Configuración de la vista // Edad
        
        age_label = Label(user_info, text = "Edad: ")
        age_label.grid(row=3, column=0)
        age_entry = Spinbox(user_info, from_=0, to=110)
        age_entry.grid(row=3, column=1)

        #Configuración de la vista // DNI
        
        id_label = Label(user_info, text = "DNI: ")
        id_label.grid(row=4, column=0)
        id_entry = Entry(user_info)
        id_entry.grid(row=4, column=1)

        #Creación de ficha // Género

        gender_label = Label(user_info, text = "Género: ")
        gender_label.grid(row=5, column=0)
        gender_entry = ttk.Combobox(user_info, values = ["Hombre", "Mujer", "No Binario", "Otro"])
        gender_entry.grid(row=5, column=1)

        #Espaciado
        for widget in user_info.winfo_children():
            widget.grid(padx=10, pady=5)

        #Checkbox
        #confirmacion = StringVar(value="Not Confirmed")
        #verificado = Checkbutton(frame, text= "He verificado la información", variable=confirmacion, onvalue= "Confirmed", offvalue="Not Confirmed")
        accept_var = IntVar(value=0)
        verificado = Checkbutton(frame, text= "He verificado la información", variable=accept_var, onvalue=1, offvalue=0)
        verificado.grid(row=2, column=0)

        #Botones
        buttons = LabelFrame(frame)
        buttons.grid(row= 3, column= 0, sticky="news", padx=20, pady=20)

        #Botón AGREGAR ALUMNO

        def insertStudent(self, name):
            self.name = name
            name = name_entry.get()
            try:
                if not name:
                    messagebox.showerror("Error")
                else:
                    name_value =  int(name)
            conn = sql.connect(BASE_DATOS)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {TABLA} ({name}) VALUES (?)")
            conn.commit()

            firstname = name_entry.get()
            lastname = last_name_entry.get()
            age = age_entry.get()
            id = id_entry.get()
            gender = gender_entry.get()
            #var = accept_var.get()

            print("First Name: ", firstname, "Last Name: ", lastname, gender, age, id)
        
        insert_button = Button(buttons, text="Agregar Alumno", command=lambda: (insertStudent(name_entry.get(), last_name_entry.get(), age_entry.get(), id_entry.get(), gender_entry.get())))
        insert_button.grid(row=1, column=0, sticky="news")

        #Botón EDITAR ALUMNO

        rewrite_button = Button(buttons, text="Editar Alumno", command=lambda: (Student.rewriteStudent(frame, variables_list, BASE_DATOS, TABLA), ))
        rewrite_button.grid(row=1, column=1)

        #Botón ELIMINAR ALUMNO

        delete_button = Button(buttons, text="Eliminar Alumno", command=lambda: (Student.deleteStudent(frame, variables_list, BASE_DATOS, TABLA), ))
        delete_button.grid(row=1, column=2)

        #Botón MOSTRAR ALUMNO

        show_button = Button(buttons, text="Mostrar Alumnos", command=lambda: (Student.showStudent(frame, variables_list, BASE_DATOS, TABLA), ))
        show_button.grid(row=1, column=3)

        #Espaciado
        for x in buttons.winfo_children():
            x.grid(padx=10, pady=5)

        #Frame List
        table = LabelFrame(frame)
        table.grid(row= 4, column= 0, sticky="news", padx=20, pady=20)

        #List

        Students_list = Listbox(table)
        Students_list.grid(row=1, column=1, sticky="news")


vista = Vista()
