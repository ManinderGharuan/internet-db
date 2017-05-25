from db import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .Country import Country
from .State import State
from .City import City


class CountryStateCity(Base):
    __tablename__ = 'country_state_city'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('country.id'))
    state_id = Column(Integer, ForeignKey('state.id'))
    city_id = Column(Integer, ForeignKey('city.id'))

    country = relationship(Country)
    state = relationship(State)
    city = relationship(City)
