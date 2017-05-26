from db import Base
from sqlalchemy import Column, Integer, String


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    name = Column(String(100))
