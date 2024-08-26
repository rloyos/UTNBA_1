'''

class Student:
    
    def createTable(self):
        conn = sql.connect(self.base_datos)
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS alumnos (
            name TEXT,
            last_name TEXT,
            age INTEGER,
            id INTEGER PRIMARY KEY,
            gender TEXT
            )""")
        conn.commit()
        conn.close

    def insertStudent(self, name, last_name):
        conn = sql.connect(self.base_datos)
        cursor = conn.cursor()
        query = (f"INSERT INTO alumnos (name, last_name) VALUES (?, ?)")
        data_insert = (name, last_name)
        cursor.execute(query, data_insert)
        conn.commit()
        conn.close()
    
    def rewriteStudent(self, name, last_name, age, id, gender):
        conn = sql.connect(self.base_datos)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {self.tabla} SET name = '{self.name}', last_name = '{self.last_name}', age = '{self.age}' WHERE id = '{self.id}'")
        conn.commit()
    
    def deleteStudent(self, id):
        self.id = id
        conn = sql.connect(self.base_datos)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.tabla} WHERE id = '{self.id}'")
        conn.commit()

    def orderedByABC(self):
        conn = sql.connect(self.base_datos)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.tabla} ORDER BY {self.last_name} DESC")
        conn.commit()

    def showStudent(self, id):
        conn = sql.connect(self.base_datos)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.tabla} WHERE id = '{id}'")
        conn.commit()

student = Student()

student.createDB()
student.createTable()'''