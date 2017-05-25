from db import Base
from sqlalchemy import Column, Integer, String


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    name = Column(String(100))

    def insert(self, session):
        """
        Insert country to database
        """
        country = session.query(Country) \
                         .filter(Country.name == self.name,
                                 Country.code == self.code) \
                         .first()

        if not country:
            country = Country(code=self.code, name=self.name)
            session.add(country)
            session.commit()

        return country
