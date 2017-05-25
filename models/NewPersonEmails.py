from db.declarative import PersonEmails


class NewPersonEmails():
    def __init__(self, person, email):
        self.person = person
        self.email = email

    def insert(self, session):
        pm = session.query(PersonEmails).filter(
            PersonEmails.person == self.person,
            PersonEmails.email == self.email).first()

        if not pm:
            pm = PersonEmails(
                person=self.person,
                email=self.email
            )

            session.add(pm)
            session.commit()

        return pm
