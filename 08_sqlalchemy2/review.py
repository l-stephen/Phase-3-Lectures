# Imports
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, validates
#initialize with decrative base
Base = declarative_base()

#Create tables
class Dog(Base):
    __tablename__ = "dogs_table"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    age = Column(Integer)
    amount_eaten = Column(Integer)

    @validates("age")
    def validate_age(self,key,value):
        if type(value) is int and value >= 0:
            return value
        else:
            raise ValueError("Not valid age")
    
    def __repr__(self):
        return f'{self.name}'

if __name__ == '__main__':
    #Create the engine
    engine = create_engine('sqlite:///animals.db')
    # Dog.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        dog = Dog(name = "Tracker", age=3, amount_eaten = 2)
        dog2 = Dog(name = "Tracker2", age=10, amount_eaten = 2)
        session.add_all([dog,dog2])
        session.commit()
        all_dogs = session.query(Dog).filter(Dog.name == "Tracker").all()
        # print(all_dogs)
        one_dog = session.query(Dog).filter(Dog.id ==2).first()
        one_dog.age = 20
        session.add(one_dog)
        session.commit()
        session.delete(one_dog)
        session.commit()