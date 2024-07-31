from modelo import Student

def main():
    createDB()
    while True:
        print("Bienvenido al sistema de gestión")
        print("1. Gestionar alumnos")
        print("2. Gestionar expedientes")
        print("3. Salir")
        option = input("Ingrese una opción: ")
        if option == "1":
            gestionar_alumnos()
        elif option == "2":
            gestionar_expedientes()
        elif option == "3":
            print("Gracias por usar el sistema")
            break
        else:
            print("Opción inválida")
    
def manage_student():
    while True:
        print("1. Crear un alumno")
        print("2. Mostrar alumnos")
        print("3. Modificar un alumno")
        print("4. Regresar al menú principal")
        op = input("Ingrese una opción: ")
        if op == "1":
            name = input("Ingrese el nombre del alumno: ")
            last_name = input("Ingrese el apellido del alumno: ")
            age = int(input("Ingrese la edad del alumno: "))
            id = input("Ingrese el DNI del alumno: ")
            phone = input("Ingrese el teléfono del alumno: ")
            email = input("Ingrese el email del alumno: ")
            address = input("Ingrese la dirección del alumno: ")
            birth = input("Ingrese la fecha de nacimiento del alumno: ")
            creation_date = input("Ingrese la fecha de creación del alumno: ")
            student = Student(name, last_name, id, phone, email, address, birth, creation_date)
            insertRow(student)
        elif op == "2":
            showStudent()
        elif op == "3":
            id = int(input("Ingrese el ID del alumno a modificar: "))
            name = input("Ingrese el nuevo nombre del alumno: ")
            last_name = input("Ingrese el nuevo apellido del alumno: ")
            age = int(input("Ingrese la nueva edad del alumno: "))
            id = input("Ingrese el nuevo DNI del alumno: ")
            phone = input("Ingrese el nuevo teléfono del alumno: ")
            email = input("Ingrese el nuevo email del alumno: ")
            address = input("Ingrese la nueva dirección del alumno: ")
            birth = input("Ingrese la nueva fecha de nacimiento del alumno: ")
            creation_date = input("Ingrese la nueva fecha de creación del alumno: ")
            rewriteRow(id, name, last_name, phone, email, address, birth, creation_date)
        elif op == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
  main()
