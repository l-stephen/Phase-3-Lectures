from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, validates

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    age = Column(Integer)
    amount_eaten = Column(Integer)

    @validates
    def validate_age(self, key, value):
        if isinstance(value, int) and value >= 0:
            return value
        else:
            raise ValueError("Must be greater than 0")
        
    def __repr__(self):
        return f'{self.name}'
    
if  __name__ == "__main__":
    engine = create_engine('sqlite:///animals.db')
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        dog = Dog(name="Tracker", age = 5, amount_eaten = 2)
        session.add(dog)
        session.commit()

    
