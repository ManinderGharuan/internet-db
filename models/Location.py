from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .CountryStateCity import CountryStateCity


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    address = Column(String(200))
    country_state_city_id = Column(Integer, ForeignKey('country_state_city.id'))
    zip_code = Column(Integer, nullable=False)

    country_state_city = relationship(CountryStateCity)
