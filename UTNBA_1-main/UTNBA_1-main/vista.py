from tkinter import ttk
from tkinter import Frame
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Spinbox
from tkinter import LabelFrame
from tkinter import StringVar
from tkinter import Menu
from tkinter import messagebox

from modelo2 import createTable, deleteTable
from modelo2 import Student, insert, list, edit, delete, show

def menu_bar(root):
    menu_bar = Menu(root)
    root.config(menu=menu_bar, width=300, height=300)
    menu_bar.add_cascade(label= "Crear Base de Datos", command= createTable) 
    menu_bar.add_cascade(label= "Eliminar Base de Datos", command=deleteTable)


class Visual(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.labels()
        self.tableDesign()


    def labels(self):

        frame = LabelFrame(self)
        frame.grid(row=0, column=0, padx=20, pady=20)

        self.name_label = Label(frame, text = "Nombre: ")
        self.name_label.grid(row=0, column=0)
        self.myName = StringVar()
        self.name_entry = Entry(frame, textvariable=self.myName)
        self.name_entry.config(width=50)
        self.name_entry.grid(row=0, column=1)

        self.last_name_label = Label(frame, text = "Apellido: ")
        self.last_name_label.grid(row=1, column=0)
        self.myLastName = StringVar()
        self.last_name_entry = Entry(frame, textvariable=self.myLastName)
        self.last_name_entry.config(width=50)
        self.last_name_entry.grid(row=1, column=1)

        self.age_label = Label(frame, text = "Edad: ")
        self.age_label.grid(row=2, column=0)
        self.myAge = StringVar()
        self.age_entry = Spinbox(frame, from_=0, to=110, textvariable=self.myAge)
        self.age_entry.config(width=49)
        self.age_entry.grid(row=2, column=1)

        self.id_label = Label(frame, text = "D.N.I.: ")
        self.id_label.grid(row=3, column=0)
        self.myId = StringVar()
        self.id_entry = Entry(frame, textvariable=self.myId)
        self.id_entry.config(width=50)
        self.id_entry.grid(row=3, column=1)

        self.gender_label = Label(frame, text = "Género: ")
        self.gender_label.grid(row=4, column=0)
        self.myGender = StringVar()
        self.gender_entry = ttk.Combobox(frame, values = ["Hombre", "Mujer", "No Binario", "Otro"], textvariable=self.myGender)
        self.gender_entry.config(width=48)
        self.gender_entry.grid(row=4, column=1)

        self.creation_label = Label(frame, text = "Fecha de Creación: ")
        self.creation_label.grid(row=5, column=0)
        self.myCreation = StringVar()
        self.creation_entry = Entry(frame, textvariable=self.myCreation)
        self.creation_entry.config(width = 50)
        self.creation_entry.grid(row=5, column=1)

        for widget in frame.winfo_children():
            widget.grid(padx=10, pady=5)

            #Botones
        buttons = LabelFrame(self)
        buttons.grid(row= 6, column= 0, sticky="news", padx=20, pady=20)

            #Botón AGREGAR ALUMNO
            
        self.insert_button = Button(buttons, text="Agregar Alumno", command = self.insertStudent)
        self.insert_button.grid(row=6, column=0)
        self.insert_button.config(fg="white", bg="#158645", cursor="hand2", activebackground="#35BD6F")


            #Botón EDITAR ALUMNO

        self.rewrite_button = Button(buttons, text="Editar Alumno", command=self.editStudents)
        self.rewrite_button.grid(row=6, column=1)
        self.rewrite_button.config(fg="black", bg="#FCE205", cursor="hand2", activebackground="#EFFD5F")

            #Botón ELIMINAR ALUMNO

        self.delete_button = Button(buttons, text="Eliminar Alumno")
        self.delete_button.grid(row=6, column=2)
        self.delete_button.config(fg="white", bg="#BD152E", cursor="hand2", activebackground="#E15370")

            #Botón MOSTRAR ALUMNO

        self.show_button = Button(buttons, text="Mostrar Alumnos")
        self.show_button.grid(row=6, column=3)
        self.show_button.config(fg="white", bg="#1658A2", cursor="hand2", activebackground="#3586DF")

            #Espaciado
        for x in buttons.winfo_children():
            x.grid(padx=10, pady=5)


            #Botones Abajo

        buttons = LabelFrame(self)
        buttons.grid(row= 8, column= 0, sticky="news", padx=20, pady=20)

            #Botón GUARDAR ALUMNO
            
        self.insert_button = Button(buttons, text="Guardar Alumno")
        self.insert_button.grid(row=6, column=0)
        self.insert_button.config(fg="white", bg="#158645", cursor="hand2", activebackground="#35BD6F", command=self.saveStudent)


            #Botón ELIMINAR ALUMNO

        self.delete_button = Button(buttons, text="Cancelar", command = self.clean)
        self.delete_button.grid(row=6, column=2)
        self.delete_button.config(fg="white", bg="#BD152E", cursor="hand2", activebackground="#E15370")

        for x in buttons.winfo_children():
            x.grid(padx=10, pady=5)

    def insertStudent(self):
        try:
            student = Student(
                self.myId.get(),
                self.myName.get(),
                self.myLastName.get(),
                self.myAge.get(),
                self.myGender.get(),
                self.myCreation.get(),
            )
            insert(student)
            self.tableDesign()
            self.clean()
        except:
            title = "Error"
            message = "Por favor crear tabla para poder agregar a los alumnos"
            messagebox.showerror(title, message)

    def deleteStudents(self):
        try:
            self.id = self.table.item(self.table.selection())['text']
            delete(self.id)
            self.clean()
            self.tableDesign()
        except:
            title = "Eliminar Datos"
            message = "No ha seleccionado ningún registro"
            messagebox.showerror(title, message)

    def showStudent(self):
        id = Student(
                self.myId.get(),
                self.myName.get(),
                self.myLastName.get(),
                self.myAge.get(),
                self.myGender.get(),
                self.myCreation.get(),
            )
        try:
            show(id)
            self.tableDesign()
            self.clean()
        except:
            title = "Error"
            message = "Por favor introducir un DNI"
            messagebox.showerror(title, message)

    def editStudents(self):
        #DISPLAY INFORMATION
        try:
            self.clean()
            self.id = self.table.item(self.table.selection())["text"]
            self.name = self.table.item(self.table.selection())["values"][0]
            self.last_name = self.table.item(self.table.selection())["values"][1]
            self.age = self.table.item(self.table.selection())["values"][2]
            self.gender = self.table.item(self.table.selection())["values"][3]
            self.creation = self.table.item(self.table.selection())["values"][4]

            self.id_entry.insert(0, self.id)
            self.name_entry.insert(0, self.name)
            self.last_name_entry.insert(0, self.last_name)
            self.age_entry.insert(0, self.age)
            self.gender_entry.insert(0, self.gender)
            self.creation_entry.insert(0, self.creation)
            edit()
            self.tableDesign()
        except:
            pass

    def saveStudent(self):
        try:
            student = Student(
                self.myId.get(),
                self.myName.get(),
                self.myLastName.get(),
                self.myAge.get(),
                self.myGender.get(),
                self.myCreation.get(),
            )
            edit(student)
            self.tableDesign()
            self.clean()
        except:
            pass
            title = "Error"
            message = "Por favor revisar los datos"
            messagebox.showerror(title, message)
    
    def disabled(self):
        self.name_entry.config(state="disabled")
        self.last_name_entry.config(state="disabled")
        self.age_entry.config(state="disabled")
        self.id_entry.config(state="disabled")
        self.gender_entry.config(state="disabled")
        self.insert_button.config(state="disabled")
        self.rewrite_button.config(state="disabled")
        self.delete_button.config(state="disabled")
        self.show_button.config(state="disabled")

    def abled(self):
        self.name_entry.config(state="normal")
        self.last_name_entry.config(state="normal")
        self.age_entry.config(state="normal")
        self.id_entry.config(state="normal")
        self.gender_entry.config(state="normal")
        self.insert_button.config(state="normal")
        self.rewrite_button.config(state="normal")
        self.delete_button.config(state="normal")
        self.show_button.config(state="normal")

    def clean(self):
        self.myName.set("")
        self.myLastName.set("")
        self.myAge.set("")
        self.myId.set("")
        self.myGender.set("")
        self.myCreation.set("")

    def tableDesign(self):
        self.list = list()

        #VER TABLA
        self.table = ttk.Treeview(self,
                                  column=("id", "name", "last_name", "age", "gender", "creation"))
        self.table.grid(row=7, column=0, sticky="nse")

        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.scroll.grid(row=7, column=4, sticky="nse")
        self.table.configure(yscrollcommand= self.scroll.set)

        #TITULOS

        self.table.heading("#0", text="DNI")
        self.table.heading("#1", text="Nombre")
        self.table.heading("#2", text="Apellido")
        self.table.heading("#3", text="Edad")
        self.table.heading("#4", text="Género")
        self.table.heading("#5", text="Fecha de Creación")

        #ITERAR ALUMNOS
        for alumno in self.list:
            self.table.insert("", 0, text=alumno[0], values=(alumno[1], alumno[2], alumno[3], alumno[4], alumno[5]))
