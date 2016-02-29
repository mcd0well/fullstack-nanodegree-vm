from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.types import Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

association_table = Table(
    'association', Base.metadata,
    Column('adopter_id', Integer, ForeignKey('adopter.id')),
    Column('puppy_id', Integer, ForeignKey('puppy.id'))
    )


class Adopter(Base):
    __tablename__ = 'adopter'
    id = Column(Integer, primary_key=True)
    puppies = relationship('Puppy', secondary=association_table, back_populates='adopters')


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    url = Column(String())
    description = Column(String())
    specialNeeds = Column(String())
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship('Puppy', uselist=False, back_populates="profile")


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)
    maxCapacity = Column(Integer, nullable=False)
    currentOccupancy = Column(Integer, nullable=False)


class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    picture = Column(String)
    dateOfBirth = Column(Date)
    gender = Column(String(8), nullable=False)
    weight = Column(Numeric(10))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship('Shelter')  # many to one
    profile = relationship('Profile', uselist=False, back_populates='puppy')  # one to one
    adopters = relationship('Adopter', secondary=association_table, back_populates='puppies')

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
