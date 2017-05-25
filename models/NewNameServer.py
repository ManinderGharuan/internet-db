from db.declarative import NameServer


class NewNameServer():
    def __init__(self, url):
        self.url = url

    def insert(self, session):
        ns = session.query(NameServer).filter(NameServer.url == self.url).first()

        if not ns:
            ns = NameServer(
                url=self.url
            )

            session.add(ns)
            session.commit()

        return ns
