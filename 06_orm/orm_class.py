#implement using a class
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

class Student:
    all = []

    def __init__(self, name, grade, id=None):
        self.id = id
        self.name = name
        self.grade = grade

    def save(self):
        sql = f'''
        INSERT INTO students(name, grade)
        VALUES ("{self.name}", {self.grade})
        '''
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def get_person(cls, name):
        sql = f'''
        SELECT * 
        FROM students
        WHERE name = "{name}"
        '''
        data = cursor.execute(sql)
        person = data.fetchone()
        print(person)
        if person:
            return Student(person[0], person[1], person[2])
        else:
            return None
    
    @classmethod
    def create_student(cls, name, grade):
        sql = f'''
        INSERT INTO students(name, grade)
        VALUES ("{name}", {grade})
        '''
        cursor.execute(sql)
        connection.commit()

    def grade_up(self):
        print("Congrats on starting the new phase!")

        self.grade = int(self.grade) + 1
        sql = f'''
        UPDATE students
        SET grade = {self.grade}
        WHERE id = {self.id}
        '''
        cursor.execute(sql)
        connection.commit()

    def delete_self(self):
        sql = f'''
        DELETE from students
        WHERE id = {self.id}
        '''

        cursor.execute(sql)
        connection.commit()


# if "__name__" == "__main__":
while True:
    user_input = input("Create or Login? ")

    if user_input == "login" or user_input == "Login":
        input2 = input("Enter your name: ")
        log = Student.get_person(input2)
        if log:
            input3 = input('''
            1) Start next phase
            2) Leave School
            ''')
            if input3 == "1":
                log.grade_up()
            if input3 == "2":
                log.delete_self()
        else:
            print("Not a valid choice")
    elif user_input == "Create" or user_input == "create":
        name = input("Enter name: ")
        grade = input("Enter Phase: ")
        Student.create_student(name, grade)




