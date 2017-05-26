from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .Location import Location
from .Organization import Organization


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    location_id = Column(Integer, ForeignKey('location.id'))
    organization_id = Column(Integer, ForeignKey('organization.id'))
    phone_number = Column(Integer)

    location = relationship(Location)
    organization = relationship(Organization)
