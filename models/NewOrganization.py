from db.declarative import Organization


class NewOrganization():
    def __init__(self, name):
        self.name = name

    def insert(self, session):
        organization = session.query(Organization).filter(
            Organization.name == self.name).first()

        if not organization:
            organization = Organization(name=self.name)

            session.add(organization)
            session.commit()

        return organization
