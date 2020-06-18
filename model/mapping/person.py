from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from exceptions import ResourceNotFound


class Person(Base):
    __tablename__ = 'People'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)

    address = Column(String(512), nullable=True)

    isAdmin = Column(Boolean, nullable=False)

    __table_args__ = (UniqueConstraint('firstname', 'lastname', 'id'),)

    def __repr__(self):
        return "<Person(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        _data = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "password": self.password,
            "email": self.email,
            "isAdmin": self.isAdmin,
            "address": self.address
        }
        return _data