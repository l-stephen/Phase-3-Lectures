from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from faker import Faker
from review import *

if __name__ == "__main__":
    engine = create_engine("sqlite:///school.db")
    Teacher.__table__.drop(engine)
    Student.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        fake = Faker()

        for _ in range(10):
            teacher = Teacher(name=fake.name(), subject = fake.word())
            session.add(teacher)

        for _ in range(20):
            student = Student(name=fake.name(), email=fake.email(), emergency_email= fake.email(), teacher_id=fake.random_int(min=1, max=10))
            session.add(student)

        session.commit()

        session.close()