#!/usr/bin/env python3
#SQL Alchemy is a powerful python library that provides a ORM
#Allows developers to interact with database using Python objects, instead of writing sql queries
#Today we will cover full CRUD operations (Create, Read, Update, Delete) using SQLAlchemy

#First you will need to install SQLAlchemy, pipenv install sqlalchemy, then pipenv shell

#import create engine, which allows you to make a connection to your database and exceute sql commands
#Then define a model, import delcarative base, session, and create a model by importing Columm, Integer, String, func()
#allows us to define classes mapped to a relational database
#the session uses sessionmaker which ensures there is a consistent identity map during your session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, validates
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Mountain(Base):
    __tablename__ = 'mountains'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    elevation = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    
    # Define one-to-many relationship with Hiker
    hikers = relationship("Hiker", back_populates="mountain")

    def __repr__(self):
        return f"{self.name}: Location {self.location}"

class Hiker(Base):
    __tablename__ = 'hikers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    experience_level = Column(String, nullable=False)
    
    # Define many-to-one relationship with Mountain
    mountain_id = Column(Integer, ForeignKey('mountains.id'))
    mountain = relationship("Mountain", back_populates="hikers")

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    @validates('experience_level')
    def validate_experience_level(self, key, experience_level):
        valid_levels = ['Beginner', 'Intermediate', 'Advanced']
        if experience_level not in valid_levels:
            raise ValueError(f"Invalid experience level. Must be one of {valid_levels}")
        return experience_level

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Define Mountain class and other necessary imports...

if __name__ == '__main__':
    # Ensure the database engine is created
    engine = create_engine('sqlite:///mountains.db')
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\nOptions:")
        print("1. Add a Mountain")
        print("2. View all Mountains")
        print("3. Update a Mountain")
        print("4. Delete a Mountain")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter mountain name: ")
            elevation = input("Enter mountain elevation: ")
            location = input("Enter mountain location: ")

            # Validate elevation input
            try:
                elevation = int(elevation)
            except ValueError:
                print("Invalid input for mountain elevation. Please enter a valid integer.")
                continue

            new_mountain = Mountain(name=name, elevation=elevation, location=location)
            session.add(new_mountain)
            session.commit()
            print("Mountain added successfully.")

        elif choice == '2':
            print("\nAll Mountains in the database:")
            for mountain in session.query(Mountain).all():
                print(mountain)

        elif choice == '3':
            mountain_id = input("Enter the ID of the mountain to update: ")
            mountain = session.query(Mountain).filter_by(id=mountain_id).first()
            if mountain:
                name = input("Enter new mountain name (press Enter to keep current value): ")
                elevation = input("Enter new mountain elevation (press Enter to keep current value): ")
                location = input("Enter new mountain location (press Enter to keep current value): ")

                if name:
                    mountain.name = name
                if elevation:
                    try:
                        mountain.elevation = int(elevation)
                    except ValueError:
                        print("Invalid input for mountain elevation. Please enter a valid integer.")
                        continue
                if location:
                    mountain.location = location

                session.commit()
                print("Mountain updated successfully.")
            else:
                print("Mountain not found.")

        elif choice == '4':
            mountain_id = input("Enter the ID of the mountain to delete: ")
            mountain = session.query(Mountain).filter_by(id=mountain_id).first()
            if mountain:
                session.delete(mountain)
                session.commit()
                print("Mountain deleted successfully.")
            else:
                print("Mountain not found.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    # Close the session
    session.close()