from db.declarative import Person


class NewPerson():
    def __init__(self, name, location, organization, phone_number):
        self.name = name
        self.location = location
        self.organization = organization
        self.phone_number = phone_number

    def insert(self, session):
        person = session.query(Person).filter(
            Person.name == self.name,
            Person.organization == self.organization).first()

        if not person:
            person = Person(
                name=self.name,
                location=self.location,
                organization=self.organization,
                phone_number=self.phone_number
            )

            session.add(person)
            session.commit()

        return person
