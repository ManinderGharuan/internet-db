from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .Person import Person
from .Registrar import Registrar


class Domain(Base):
    __tablename__ = 'domain'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    creation_date = Column(DateTime, nullable=False)
    last_update_date = Column(DateTime, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    registrar_id = Column(Integer, ForeignKey('registrar.id'))
    referral_url = Column(String(100))
    whois_server = Column(String(100))
    status = Column(String(300))

    person = relationship(Person)
    registrar = relationship(Registrar)
