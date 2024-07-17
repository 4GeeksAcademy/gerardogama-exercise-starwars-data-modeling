import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Float

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(32))

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(50))
    terrain = Column(String(50))    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))   
    last_name = Column(String(50))
    height = Column(Float)
    mass = Column(Integer)
    birht_year = Column(String(50))
    gender = Column(String(20))



class Starships(Base):
    __tablename__= 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))
    model = Column(String(50))
    manufacturer = Column(String(50))
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    consumables = Column(String(50))

class FavoritesPlanets(Base):
    __tablename__= "favorites_planets"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_id_relationship = relationship(Planets)

class FavoritesCharacters(Base):
    __tablename__='favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    user_id_relationship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id_relationship = relationship(Characters)   

class FavoriteStarships(Base):
    __tablename__= "favorites_starships"    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships_id_ralationship = relationship(Starships)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')