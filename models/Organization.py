from db import Base
from sqlalchemy import Column, Integer, String


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
