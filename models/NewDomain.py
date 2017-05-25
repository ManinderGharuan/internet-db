from db.declarative import Domain


class NewDomain():
    def __init__(self, name, creation_date, last_update_date, expiration_date,
                 person, registrar, referral_url, whois_server, status):
        self.name = name
        self.creation_date = creation_date
        self.last_update_date = last_update_date
        self.expiration_date = expiration_date
        self.person = person
        self.registrar = registrar
        self.referral_url = referral_url
        self.whois_server = whois_server
        self.status = status

    def insert(self, session):
        domain = session.query(Domain).filter(
            Domain.name == self.name,
            Domain.person == self.person).first()

        if not domain:
            domain = Domain(
                name=self.name,
                creation_date=self.creation_date,
                last_update_date=self.last_update_date,
                expiration_date=self.expiration_date,
                person=self.person,
                registrar=self.registrar,
                referral_url=self.referral_url,
                whois_server=self.whois_server,
                status=self.status
            )

            session.add(domain)
            session.commit()

        return domain
