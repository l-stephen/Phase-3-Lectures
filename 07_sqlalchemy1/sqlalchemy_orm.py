#Start with imports
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base
#Define declarative_base()
Base = declarative_base()
#create a class that is a child of Base
class Student(Base):

    #create a table name
    __tablename__ = "students"
    #create models
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer)
    #create a validation

    #create a repr

#create a class that is a child of BASE
class Teacher(Base):
    #create a table name
    __tablename__ = "teachers"
    #create models
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    phone = Column(Integer)
    email = Column(String)

    #create a validation

    #create a repr

if __name__ == "__main__":
    #create the database engine with create_engine()
    engine = create_engine("sqlite:///classroom.db")
    #delete tables using .drop(engine)
    Student.__table__.drop(engine)
    Teacher.__table__.drop(engine)
    #Create the table with create_all()
    Base.metadata.create_all(engine)
    #with Session object create a session
    with Session(engine) as session:
        ''' 
        The session object will allow use to perform CRUD on our models
        Session.add()
        Session.add_all([])
        Session.query()
            .all()
            .orderby() ex: Table.name.desc()
            .limit()  ex: limit(2)
            .filter() ex Table.name = "name"
            .update() ex {Table.name: newname}
        Session.delete()
        Session.commit()
        '''
        #query all students from the database, use order_by() and sort in asc order, use limit() and all()
        all_students = session.query(Student).order_by(Student.full_name.asc()).limit(2).all()
        #take user input for a name
        search_student = input("Enter a students name: ")
        #query from the student database using user input, use filter() and first()
        search = session.query(Student).filter(Student.full_name == search_student).first()
        #if the student exists, delete them from the session
        if search:
            print("Student Exists")
            session.delete(search)
            session.commit()

        #commit the change!

        #else print not a student
        else:
            print("Not a student")

        #take in user input to create a new student
        new_student = input("Enter a new Student: ")
        n_student = Student(full_name = new_student)
        #take in user input to create a new teacher
        new_teacher = input("Enter a teacher: ")
        n_teacher = Teacher(full_name = "Stephen Lambert", phone = 1234567890, email="stephen.lambert@flatironschool.com")
        #demonstrate add() and add_all()
        session.add_all([n_student, n_teacher])
        session.commit()
        #commit the change!
















