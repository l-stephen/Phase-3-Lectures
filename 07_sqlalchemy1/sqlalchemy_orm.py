#SQL Alchemy is a powerful python library that provides a ORM
#Allows developers to interact with database using Python objects, instead of writing sql queries
#Today we will cover full CRUD operations (Create, Read, Update, Delete) using SQLAlchemy

#First you will need to install SQLAlchemy, pipenv install sqlalchemy, then pipenv shell

#import create engine, which allows you to make a connection to your database and exceute sql commands
#Then define a model, import delcarative base, session, and create a model by importing Columm, Integer, String, func()
#allows us to define classes mapped to a relational database
#the session uses sessionmaker which ensures there is a consistent identity map during your session

#start by setting up declarative_base()

#create a class that is a child of BASE

    #create a table name

    #create models

#create a class that is a child of BASE

    #create a table name

    #create models

    #create a __repr__ to make it easy to see results

#if main create the database engine 


    #create the database schema using create_all

    #create a session

    #add to the database and commit


    #query from the session, delete from the session and commit
















