from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from sqlalchemy_orm import *

# Define your Mountain and Hiker classes and other necessary imports here...

if __name__ == '__main__':
    # Ensure the database engine is created
    engine = create_engine('sqlite:///mountains.db')
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    num_mountains = 100  # Define the number of mountains to create

    # Generate fake data for mountains using Faker and range
    for _ in range(10):
        mountain = Mountain(name=fake.word(), elevation=fake.random_int(min=1000, max=5000), location=fake.country())
        session.add(mountain)

        

    for _ in range(10):
        hiker = Hiker(name=fake.name(), experience_level=random.choice(['Beginner', 'Intermediate', 'Advanced']), mountain=mountain)
        session.add(hiker)

    session.commit()
    print(" mountains and hikers added successfully.")

    # Close the session
    session.close()
