from db import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .Domain import Domain
from .NameServer import NameServer


class DomainNameServers(Base):
    __tablename__ = 'domain_name_servers'

    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey('domain.id'))
    name_server_id = Column(Integer, ForeignKey('name_server.id'))

    domain = relationship(Domain)
    name_server = relationship(NameServer)
