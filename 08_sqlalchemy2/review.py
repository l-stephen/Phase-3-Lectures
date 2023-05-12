#!/usr/bin/env python3
#Import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

#initialize declarative base
Base = declarative_base()
#create a meal class and inheret from base
class Meal(Base):
    __tablename__ = "Meals"
    #Properties
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    temp = Column(Integer())
    calories = Column(Integer())

#create a ingredients class and inheret from base
class Ingredient(Base):
    __tablename__ = "Ingredients"
    id = Column(Integer(), primary_key=True)
    name = Column(String())

#create a method that creates your tables
def create_tables():
    #Create the engine
    engine = create_engine('sqlite:///food.db')
    #Create the tables based on out parent base
    Base.metadata.create_all(engine)

#create a method to add a meal
def add(meal):
    print(meal.name)
    # Create the engine
    engine = create_engine('sqlite:///food.db')
    # Create a session from that engine (Allowing us to create tables)
    with Session(engine) as session:
        # Using .add we can now add an object
        session.add(meal)
        # Make sure to commit
        session.commit()

#create a method to get all of the data
def select():
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        meal_list = session.query(Meal).limit(2).all()
    # Now we can get all of that table using .query and .all
    return meal_list

#create a method to update the database
def update():
    #Updating formatting {attribute: new_attribute}
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        session.query(Meal).update({Meal.temp: Meal.temp+1})
        session.commit()

#create a method to delete the data
def delete(temp_delete):
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        session.query(Meal).filter(Meal.temp == temp_delete).delete()
        # session.delete(filtered_list)
        session.commit()

#Create a method to delete all data and remake the database
def remake_tables():
    engine = create_engine('sqlite:///food.db')
    Meal.__table__.drop(engine)
    Base.metadata.create_all(engine)

#if name is main create tables, create meals, and test methods
if __name__ == '__main__':
    create_tables()
    newmeal= Meal(
        name = "Spinach Puffs",
        temp = 90,
        calories = 200
    )
    rice= Meal(
        name = "Rice",
        temp = 100,
        calories = 300
    )
    remake_tables()
    add(rice)
    add(newmeal)
    delete(100)
    update()
    meal_list = select()
    for meal in meal_list:
        print(meal.name, meal.temp, meal.calories)
    