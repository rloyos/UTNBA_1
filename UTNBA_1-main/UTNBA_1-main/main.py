from vista import Visual, menu_bar
from tkinter import Tk

def main():
    root = Tk()
    root.title("Tabla de Alumnos")
    root.resizable(0,0)
    menu_bar(root)

    app = Visual(root = root)

    app.mainloop()

if __name__ == "__main__":
    main()
