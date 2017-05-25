from db import Base
from sqlalchemy import Column, Integer, String


class State(Base):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    def insert(self, session):
        state = session.query(State).filter(State.name == self.name).first()

        if not state:
            state = State(name=self.name)

            session.add(state)
            session.commit()

        return state
