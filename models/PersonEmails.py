from db import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .Person import Person
from .Email import Email


class PersonEmails(Base):
    __tablename__ = 'person_emails'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    email_id = Column(Integer, ForeignKey('email.id'))

    person = relationship(Person)
    email = relationship(Email)
