from db import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
