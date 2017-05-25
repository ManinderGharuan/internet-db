from db import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
import City
import State
import Country


class CountryStateCity(Base):
    __tablename__ = 'country_state_city'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('country.id'))
    state_id = Column(Integer, ForeignKey('state.id'))
    city_id = Column(Integer, ForeignKey('city.id'))

    country = relationship(Country)
    state = relationship(State)
    city = relationship(City)

    def insert(self, session):
        """
        Insert country to database
        """
        csc = session.query(CountryStateCity).filter(
            CountryStateCity.country == self.country,
            CountryStateCity.state == self.state,
            CountryStateCity.city == self.city).first()

        if not csc:
            csc = CountryStateCity(country=self.country,
                                   state=self.state,
                                   city=self.city)
            session.add(csc)
            session.commit()

        return csc
