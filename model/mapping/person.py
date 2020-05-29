from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from model.mapping.address import Address
from model.mapping.sport import SportAssociation
from exceptions import ResourceNotFound


class Person(Base):
    __tablename__ = 'people'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    person_type = Column(String(50), nullable=False)
    address_id = Column(String(36), ForeignKey("addresses.id"), nullable=True)

    address = relationship("Address", cascade="all,delete-orphan", single_parent=True)
    sports = relationship("SportAssociation", back_populates="person")

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
            "sports": []
        }
        for sport_association in self.sports:
            _data['sports'].append({"level": sport_association.level,
                                    "id": sport_association.sport.id,
                                    "name": sport_association.sport.name})

        if self.address is not None:
            _data['address'] = {
                "street": self.address.street,
                "postal_code": self.address.postal_code,
                "city": self.address.city,
                "country": self.address.country
            }
        return _data

    def set_address(self, street: str, postal_code: str, city: int, country: str = 'FRANCE'):
        self.address = Address(street=street, city=city, postal_code=postal_code, country=country)

    def add_sport(self, sport, level, session):
        asoociation = SportAssociation(level=level)
        asoociation.sport = sport
        self.sports.append(asoociation)
        session.flush()

    def delete_sport(self, sport, session):
        sport_association = None
        for association in self.sports:
            if association.sport == sport:
                sport_association = association
                break
        if sport_association is not None:
            self.sports.remove(sport_association)
            session.delete(sport_association)
            session.flush()
