from db import Base
from sqlalchemy import Column, Integer, String


class State(Base):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
