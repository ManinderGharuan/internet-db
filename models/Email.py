from db import Base
from sqlalchemy import Column, Integer, String


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
