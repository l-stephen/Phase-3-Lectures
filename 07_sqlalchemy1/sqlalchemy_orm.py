#!/usr/bin/env python3
#SQL Alchemy is a powerful python library that provides a ORM
#Allows developers to interact with database using Python objects, instead of writing sql queries
#Today we will cover full CRUD operations (Create, Read, Update, Delete) using SQLAlchemy

#First you will need to install SQLAlchemy, pipenv install sqlalchemy, then pipenv shell

#import create engine, which allows you to make a connection to your database and exceute sql commands
#Then define a model, import delcarative base, session, and create a model by importing Columm, Integer, String, func()
#allows us to define classes mapped to a relational database
#the session uses sessionmaker which ensures there is a consistent identity map during your session
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#start by setting up declarative_base()
Base = declarative_base()
#create a class that is a child of BASE
class Mountains(Base):

    #create a table name
    __tablename__ = 'mountains'
    #create models
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    elevation = Column(Integer())
    location = Column(String())

    def __repr__(self):
        return f"{self.name}: Location {self.location}"
    
#if main, create the database engine 
if __name__ == '__main__':
    engine = create_engine('sqlite:///moutnains.db')
    #create the database schema using create_all
    Base.metadata.create_all(engine)
    #create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    #delete the session data first
    #session.query(Mountains).delete()
    #add to the database and commit
    mountain1 = Mountains(
        name = 'Mount Everest',
        elevation = 29029,
        location = 'Nepal'
    )

    mountain2 = Mountains(
        name = 'Mount Fuji',
        elevation = 12388,
        location = 'Japan'
    )

    print(mountain1, mountain2)
    session.bulk_save_objects([mountain1, mountain2])
    session.commit()
    #query from the session, delete from the session and commit


















