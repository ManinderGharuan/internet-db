from db import Base
from sqlalchemy import Column, Integer, String


class Registrar(Base):
    __tablename__ = 'registrar'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    phone_number = Column(Integer)
    url = Column(String(200))
