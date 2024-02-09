from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker, relationship, validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    temp = Column(Integer(), nullable=False)
    calories = Column(Integer(), nullable=False)
    #using backref
    #ingredients = relationship('Ingredient', secondary='recipes', backref='meals')  
    ingredients = relationship('Ingredient', secondary='recipes', back_populates='meals')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Meal name cannot be empty.")
        return name

    @validates('temp')
    def validate_temp(self, key, temp):
        if temp < 0:
            raise ValueError("Temperature must be a positive integer.")
        return temp

    @validates('calories')
    def validate_calories(self, key, calories):
        if calories < 0:
            raise ValueError("Calories must be a positive integer.")
        return calories

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    #using backref
    #meals = relationship('Meal', secondary='recipes', backref='ingredients') 
    meals = relationship('Meal', secondary='recipes', back_populates='ingredients')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Ingredient name cannot be empty.")
        return name

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer(), primary_key=True)
    meal_id = Column(Integer(), ForeignKey('meals.id'))
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'))

engine = create_engine('sqlite:///many_to_many.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

with Session() as session:
    # Create a new meal
    new_meal = Meal(name="Spaghetti", temp=90, calories=350)
    session.add(new_meal)
    session.commit()

    # Create a new ingredient
    new_ingredient = Ingredient(name="Tomato Sauce")
    session.add(new_ingredient)
    session.commit()

    # Add the new ingredient to the meal
    new_recipe = Recipe(meal_id=new_meal.id, ingredient_id=new_ingredient.id)
    session.add(new_recipe)
    session.commit()

    # Remove the ingredient from the meal
    recipe_to_delete = session.query(Recipe).filter_by(meal_id=new_meal.id, ingredient_id=new_ingredient.id).first()
    session.delete(recipe_to_delete)
    session.commit()

    # Delete the meal
    meal_to_delete = session.query(Meal).filter_by(id=new_meal.id).first()
    session.delete(meal_to_delete)
    session.commit()

    # Get all meals
    all_meals = session.query(Meal).all()
    for meal in all_meals:
        print(f"Meal ID: {meal.id}, Name: {meal.name}, Temperature: {meal.temp}, Calories: {meal.calories}")
