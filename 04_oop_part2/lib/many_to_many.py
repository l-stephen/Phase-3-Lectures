class Lecture:
    def __init__(self, topic, teacher, location ):
        self.topic = topic
        self.teacher = teacher
        self.location = location
        self.students = []

    def addStudent(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            student.lectures.append(self)

class Student:
    def __init__(self, name, phase): 
        self.name = name
        self.phase = phase
        self.lectures = []

    def __repr__(self):
        return self.name
    
if __name__=="__main__":
    js = Lecture("Javasript Clases", "Sam", "Red Room")
    reactAlts = Lecture("React alternatives", "Sam", "Blue Room")
    python = Lecture("Python Tips", "David", "Blue Room")

    dane = Student("Dane", "Phase 3")
    dylan = Student("Dylan", "Phase 3")
    lydia = Student("Lydia", "Phase 3")
    kaleb = Student("Kaleb", "Phase 3")
    danny = Student("Danny", "Phase 3")
    taylor = Student("taylor", "Phase 3")

    python.addStudent(dane)
    python.addStudent(dylan)
    python.addStudent(lydia)

    reactAlts.addStudent(kaleb)
    reactAlts.addStudent(danny)
    reactAlts.addStudent(taylor)


    print(reactAlts.students)
    print(python.students)


    
