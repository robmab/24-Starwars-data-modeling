import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    name = Column(String(10), nullable=False)
    last_name = Column(String(10), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    favourites_persons = relationship(
        "Favourites_persons", backref='persons', lazy=True)
    favourites_vehicles = relationship(
        "Favourites_vehicles", backref='persons', lazy=True)
    favourites_planets = relationship(
        "Favourites_planets", backref='persons', lazy=True)


class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)

    name = Column(String(10), unique=True, nullable=False)
    gender = Column(String(10), nullable=False)
    birth_year = Column(String(10), nullable=False)
    eye_color = Column(String(10), nullable=False)
    hair_color = Column(String(10), nullable=False)
    mass = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)

    favourites_persons = relationship(
        "Favourites_persons", backref='persons', lazy=True)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)

    name = Column(String(20), unique=True, nullable=False)
    model = Column(String(20), nullable=False)
    vehicle_class = Column(String(20), nullable=False)
    manufacturer = Column(String(20), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(20), nullable=False)

    favourites_vehicles = relationship(
        "Favourites_vehicles", backref='vehicles', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

    name = Column(String(20), unique=True, nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(20), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(20), nullable=False)
    terrain = Column(String(20), nullable=False)
    surface_water = Column(Integer, nullable=False)

    favourites_planets = relationship(
        "Favourites_planets", backref='planets', lazy=True)


# FAVOURITES
class Favourites_persons(Base):
    __tablename__ = 'favourites_persons'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'), nullable=False)


class Favourites_vehicles(Base):
    __tablename__ = 'favourites_vehicles'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)


class Favourites_planets(Base):
    __tablename__ = 'favourites_planets'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
