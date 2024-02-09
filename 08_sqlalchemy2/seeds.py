from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from review import Teacher, Student, Base

if __name__ == "__main__":
    # Ensure the database engine is created
    engine = create_engine('sqlite:///school.db')
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    # Generate fake data for teachers using Faker and range
    for _ in range(5):
        teacher = Teacher(name=fake.name(), subject=fake.word())
        session.add(teacher)

    # Generate fake data for students using Faker and range
    for _ in range(20):
        student = Student(name=fake.name(), email=fake.email(), emergency_email=fake.email(), teacher_id=fake.random_int(min=1, max=5))
        session.add(student)

    session.commit()
    print("Teachers and students added successfully.")

    # Close the session
    session.close()

