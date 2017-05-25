from db.declarative import DomainNameServers


class NewDomainNameServers():
    def __init__(self, domain, server):
        self.domain = domain
        self.server = server

    def insert(self, session):
        dns = session.query(DomainNameServers).filter(
            DomainNameServers.domain == self.domain,
            DomainNameServers.name_server == self.server).first()

        if not dns:
            dns = DomainNameServers(
                domain=self.domain,
                name_server=self.server
            )

            session.add(dns)
            session.commit()

        return dns
