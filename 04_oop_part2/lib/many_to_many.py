class Lecture:
    def __init__(self, topic, teacher, location ):
        self.topic = topic
        self.teacher = teacher
        self.location = location
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            student.lectures.append(self)

class Student:
    def __init__(self, name, phase): 
        self.name = name
        self.phase = phase
        self.lectures = []
        self.grades = {}  # Dictionary to store grades for each lecture

    def __repr__(self):
        return self.name
    
    def add_grade(self, lecture, grade):
        self.grades[lecture.topic] = grade

    @classmethod
    def calculate_average_grades(cls):
        total_grades = 0
        total_lectures = 0
        total_students = 0
        for student in cls.students:
            total_students += 1
            for grade in student.grades.values():
                total_grades += grade
                total_lectures += 1
        if total_students == 0:
            return 0  # Avoid division by zero
        return total_grades / total_lectures

if __name__=="__main__":
    js = Lecture("Javascript Classes", "Sam", "Red Room")
    reactAlts = Lecture("React Alternatives", "Sam", "Blue Room")
    python = Lecture("Python Tips", "David", "Blue Room")

    alice = Student("Alice", "Phase 3")
    bob = Student("Bob", "Phase 3")
    charlie = Student("Charlie", "Phase 3")
    david = Student("David", "Phase 3")
    emma = Student("Emma", "Phase 3")
    frank = Student("Frank", "Phase 3")

    python.add_student(alice)
    python.add_student(bob)
    python.add_student(charlie)

    reactAlts.add_student(david)
    reactAlts.add_student(emma)
    reactAlts.add_student(frank)

    alice.add_grade(python, 90)
    alice.add_grade(reactAlts, 85)
    bob.add_grade(python, 95)
    bob.add_grade(reactAlts, 91)
    charlie.add_grade(python, 88)
    charlie.add_grade(reactAlts, 92)

    all_students = [alice, bob, charlie, david, emma, frank]
    total_average_grade = Student.calculate_average_grades()
    print("Average Grades for all students:", total_average_grade)
