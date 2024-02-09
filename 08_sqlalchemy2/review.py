from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, validates


Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    #using backref 
    # students = relationship("Student", backref=backref("teacher"))
    students = relationship("Student", back_populates="teacher")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    emergency_email = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="students")

    @validates('email', 'emergency_email')
    def validate_email(self, key, value):
        if type(value) is str and "@" in value:
            if key == 'emergency_email' and self.email == value:
                raise ValueError("Cannot have the same emergency email and email")
            return value
        else:
            raise ValueError(f"Not valid {key}")

if __name__ == "__main__":
    engine = create_engine("sqlite:///school.db")
    Student.__table__.drop(engine)
    Teacher.__table__.drop(engine)
    Base.metadata.create_all(engine)


    with Session(engine) as session:
        # Creating teachers
        math_teacher = Teacher(name="Mr. Smith", subject="Math")
        science_teacher = Teacher(name="Ms. Johnson", subject="Science")
        session.add_all([math_teacher, science_teacher])
        session.commit()

        # Creating students
        jack = Student(name="Jack", email="jack@jack.com", emergency_email="jack2@jack.com", teacher_id=math_teacher.id)
        emmi = Student(name="Emmi", email="emmi@emmi.com", emergency_email="emergency@gmail.com", teacher_id=science_teacher.id)
        session.add_all([jack, emmi])
        session.commit()

        # Read students
        students = session.query(Student).all()
        for student in students:
            print(f"{student.name} - Teacher: {student.teacher.name}")

        # Update student
        jack.name = "Jack Smith"
        session.commit()

        # Delete student
        session.delete(emmi)
        session.commit()

        # Read updated students
        students = session.query(Student).all()
        for student in students:
            print(f"{student.name} - Teacher: {student.teacher.name}")

    session.close()
