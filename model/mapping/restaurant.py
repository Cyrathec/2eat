from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from model.mapping.address import Address
from model.mapping.produit import ProduitAssociation
from exceptions import ResourceNotFound


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    restaurant_name= Column(String(50), nullable=False)
    #lastname = Column(String(50), nullable=False)
    #email = Column(String(256), nullable=False)
    #person_type = Column(String(50), nullable=False)
    address_id = Column(String(36), ForeignKey("addresses.id"), nullable=True)

    address = relationship("Address", cascade="all,delete-orphan", single_parent=True)
    produits = relationship("ProduitAssociation", back_populates="restaurant")

    __table_args__ = (UniqueConstraint('restaurant_name'),)
    # https://docs.sqlalchemy.org/en/13/orm/inheritance.html
    
    def __repr__(self):
        return "<Restaurant(%s)>" % (self.restaurant_name.upper())

    def to_dict(self):
        _data = {
            "id": self.id,
            "restaurant_name": self.restaurant_name,
            #"lastname": self.lastname,
            #"email": self.email,
            #"type": self.person_type,
            "produits": []
        }
        for produit_associations in self.produits:
            _data['produits'].append({
                                    "id": produit_associations.produits.id,
                                    "name": produit_associations.produits.name})

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
