from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'))
    organization_id = Column(Integer, ForeignKey('organization.id'))
    phone_number = Column(Integer)

    location = relationship(Location)
    organization = relationship(Organization)


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)


class PersonEmails(Base):
    __tablename__ = 'person_emails'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    email_id = Column(Integer, ForeignKey('email.id'))

    person = relationship(Person)
    email = relationship(Email)


class Registrar(Base):
    __tablename__ = 'registrar'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(Integer)
    url = Column(String(200))


class NameServer(Base):
    __tablename__ = 'name_server'

    id = Column(Integer, primary_key=True)
    url = Column(String(200), nullable=False)


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


class DomainNameServers(Base):
    __tablename__ = 'domain_name_servers'

    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey('domain.id'))
    name_server_id = Column(Integer, ForeignKey('name_server.id'))

    domain = relationship(Domain)
    name_server = relationship(NameServer)


