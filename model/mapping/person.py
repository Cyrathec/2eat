from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from exceptions import ResourceNotFound


class Person(Base):
    __tablename__ = 'people'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    person_type = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)

    address = Column(String(255), nullable=False)

    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)
    # https://docs.sqlalchemy.org/en/13/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': person_type
    }

    def __repr__(self):
        return "<Person(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        _data = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "type": self.person_type,
            "address":self.address
        }
        return _data