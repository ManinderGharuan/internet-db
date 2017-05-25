from db.declarative import Registrar


class NewRegistrar():
    def __init__(self, name, phone_number, url):
        self.name = name
        self.phone_number = phone_number
        self.url = url

    def insert(self, session):
        registrar = session.query(Registrar).filter(
            Registrar.name == self.name,
            Registrar.url == self.url).first()

        if not registrar:
            registrar = Registrar(
                name=self.name,
                phone_number=self.phone_number,
                url=self.url
            )

            session.add(registrar)
            session.commit()

        return registrar
