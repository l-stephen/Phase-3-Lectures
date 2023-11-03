from faker import Faker
from random import randint
from relationships import Animal, Zoo, Zookeeper, engine, Base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

fake = Faker()
Animal.__table__.drop(engine)
Zookeeper.__table__.drop(engine)
Zoo.__table__.drop(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    all_zoo = []

    for i in range(10):
        zoo = Zoo(name=fake.name(), location = fake.address())
        all_zoo.append(zoo)

    all_zookeeper = []
    for i in range(10):
        person = Zookeeper(name=fake.name(), email= fake.email())
        all_zookeeper.append(person)

    all_animals = []
    for i in range(10):
        animal = Animal(species = fake.name(), zoo_id = randint(1,10), zookeeper_id=randint(1,10))
        all_animals.append(animal)

    session.add_all(all_zoo)
    session.add_all(all_zookeeper)
    session.add_all(all_animals)
    session.commit()
