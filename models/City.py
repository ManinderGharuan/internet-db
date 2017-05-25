from db import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    def insert(self, session):
        city = session.query(City).filter(City.name == self.name).first()

        if not city:
            city = City(name=self.name)

            session.add(city)
            session.commit()

        return city
