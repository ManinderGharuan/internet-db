from db.declarative import Email


class NewEmail():
    def __init__(self, email):
        self.email = email

    def insert(self, session):
        email = session.query(Email).filter(Email.email == self.email).first()

        if not email:
            email = Email(email=self.email)

            session.add(email)
            session.commit()

        return email
