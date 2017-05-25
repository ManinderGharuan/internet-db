from db import Base
from sqlalchemy import Column, Integer, String


class NameServer(Base):
    __tablename__ = 'name_server'

    id = Column(Integer, primary_key=True)
    url = Column(String(200), nullable=False)
