class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll(self, student):
        self.students.append(student)
        student.courses.append(self)


# Create some students and courses
s1 = Student("Alice")
s2 = Student("Bob")
c1 = Course("Math")
c2 = Course("Science")

# Enroll the students in the courses
s1.enroll(c1)
s1.enroll(c2)
s2.enroll(c1)

# Print the list of courses for each student
print(s1.name, "is enrolled in:")
for course in s1.courses:
    print(course.name)

print(s2.name, "is enrolled in:")
for course in s2.courses:
    print(course.name)

# Print the list of students for each course
print(c1.name, "has the following students:")
for student in c1.students:
    print(student.name)

print(c2.name, "has the following students:")
for student in c2.students:
    print(student.name)

