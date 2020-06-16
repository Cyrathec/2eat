from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from model.mapping.address import Address
from exceptions import ResourceNotFound


class Person(Base):
    __tablename__ = 'people'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    person_type = Column(String(50), nullable=True)
    password = Column(String(256), nullable=False)

    address_id = Column(String(256), nullable=True)

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
            "type": self.person_type
        }
        

        if self.address_id is not None:
            _data['address'] = self.address_id
            
        return _data

    def set_address(self, street: str, postal_code: str, city: int, country: str = 'FRANCE'):
        self.address = Address(street=street, city=city, postal_code=postal_code, country=country)


    