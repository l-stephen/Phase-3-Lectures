from sqlalchemy import ForeignKey, Column, Integer, String, Float, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, validates

Base = declarative_base()
# one to many relationship
class PencilCase(Base):
    __tablename__ = "pencil_cases"
    id = Column(Integer, primary_key=True)
    cap = Column(Integer)
    color = Column(String)
    pencils = relationship("Pencil", back_populates='pencil_case')

class Pencil(Base):
    __tablename__ = "pencils"
    id = Column(Integer, primary_key=True)
    size = Column(Float)
    color = Column(String)
    pencil_case_id = Column(Integer, ForeignKey('pencil_cases.id'))
    # pencil_case = relationship('PencilCase', backref = 'pencils')
    pencil_case = relationship("PencilCase", back_populates="pencils")

engine = create_engine("sqlite:///one_to_many.db")
Base.metadata.create_all(engine)
with Session(engine) as session:
    pc = PencilCase(cap=100, color="Red")
    p1 = Pencil(size=0.5, color="Blue", pencil_case = pc)
    p2 = Pencil(size=0.7, color="Red", pencil_case = pc)
    p3 = Pencil(size=0.6, color="Black", pencil_case=pc)
    session.add_all([pc, p1, p2, p3])
    session.commit()
    case = session.query(PencilCase).first()
    print(case)

Base = declarative_base()
class Zoo(Base):
    __tablename__ = "zoos"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    animals = relationship("Animal", back_populates="zoo")
    zookeepers = relationship("Zookeeper", secondary="animals", back_populates="zoos", viewonly=True)

class Zookeeper(Base):
    __tablename__ = "zookeepers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    animals = relationship("Animal", back_populates="zookeeper")
    zoos = relationship("Zoo", secondary="animals", back_populates="zookeepers", viewonly=True)


class Animal(Base):
    __tablename__="animals"
    id = Column(Integer, primary_key=True)
    species = Column(String)
    zoo_id = Column(Integer, ForeignKey("zoos.id"))
    zookeeper_id = Column(Integer, ForeignKey("zookeepers.id"))
    zoo = relationship("Zoo", back_populates="animals")
    zookeeper = relationship("Zookeeper", back_populates="animals")

#With backref
# class Zoo(Base):
#     __tablename__ = "zoos"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     location = Column(String)
#     animals = relationship("Animal", backref="zoo")
#     zookeepers = relationship("Zookeeper", secondary="animals", backref="zoos", viewonly=True)

# class Zookeeper(Base):
#     __tablename__ = "zookeepers"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String)
#     animals = relationship("Animal", backref="zookeeper")
#     zoos = relationship("Zoo", secondary="animals", backref="zookeepers", viewonly=True)

# class Animal(Base):
#     __tablename__ = "animals"
#     id = Column(Integer, primary_key=True)
#     species = Column(String)
#     zoo_id = Column(Integer, ForeignKey("zoos.id"))
#     zookeeper_id = Column(Integer, ForeignKey("zookeepers.id"))

engine = create_engine('sqlite:///many_to_many.db')
Base.metadata.create_all(engine)
with Session(engine) as session:
    zoo_nyc = Zoo(name = "Central Park Zoo", location = "NY")
    zoo_den = Zoo(name = "Denver Zoo", location = "Den")
    zookeeper_dylan = Zookeeper(name="Dylan", email="dylan@gmail.com")
    animal1 = Animal(species="Lion", zoo = zoo_nyc, zookeeper = zookeeper_dylan)
    animal2 = Animal(species="Giraffe", zoo = zoo_den, zookeeper = zookeeper_dylan)
    session.add_all([zoo_nyc, zoo_den, animal1, animal2, zookeeper_dylan])
    session.commit()




    







