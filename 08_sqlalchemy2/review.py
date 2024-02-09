from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, validates

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer(), primary_key=True)
    name = Column(String, nullable = False)
    subject = Column(String, nullable=False)

    students = relationship("Student", back_populates="teacher")
    # students = relationship("Student", backref="teacher")

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    emergency_email = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="students")

    @validates("email", "emergency_email")
    def validate_email(self, key, value):
        if type(value) is str and "@" in value:
           if key == "emergency_email" and self.email == value: 
               raise ValueError("Cannot have the same email")
           else:
               return value
        else:
            raise ValueError(f"Not valid {key}")
        
if __name__ == "__main__":
    engine = create_engine("sqlite:///school.db")
    # Student.__table__.drop(engine)
    # Teacher.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        #create
        david = Teacher(name="David Doan", subject="CS")
        stephen = Teacher(name="Stephen Lambert", subject="CS")
        session.add_all([david, stephen])
        session.commit()
        #create
        kyle= Student(name="Kyle", email="kyle@gmail.com", emergency_email="emergency@gmail.com", teacher_id = stephen.id)
        nick= Student(name="Nick", email="nick@gmail.com", emergency_email="emergency@gmail.com", teacher_id=david.id)
        test_student = Student(name="test", email="test@gmail.com", emergency_email="emergency@gmail.com", teacher_id=david.id)
        session.add_all([kyle, nick, test_student])
        session.commit()
        
        #read
        students = session.query(Student).all()
        print(students)
        for student in students:
            print(student)
            print(f"{student.name} - Teacher: {student.teacher.name}")

        #update
        stephen.name = "John"
        session.commit()

        #delete
        session.delete(test_student)
        session.commit()

        students2 = session.query(Student).all()
        for student in students2:
            print(f"{student.name} - Teacher:{student.teacher.name}")







