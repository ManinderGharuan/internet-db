from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import City
import State
import Country


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    address = Column(String(200), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    state_id = Column(Integer, ForeignKey('state.id'))
    country_id = Column(Integer, ForeignKey('country.id'))
    zip_code = Column(Integer, nullable=False)

    city = relationship(City)
    state = relationship(State)
    country = relationship(Country)

    def insert(self, session):
        location = session.query(Location).filter(
            Location.address == self.address,
            Location.country_state_city == self.country_state_city).first()

        if not location:
            location = Location(
                address=self.address,
                country_state_city=self.country_state_city,
                zip_code=self.zip_code
            )

            session.add(location)
            session.commit()

        return location
