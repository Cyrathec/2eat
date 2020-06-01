from model.mapping import Base
import uuid

from sqlalchemy import Table, Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'order'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    restaurant = Column(String(36), ForeignKey('Restaurant.id'))                        # ForeignKey to the Restaurant id
    client = Column(String(36), ForeignKey('Person.id'))                                # ForeignKey to the client id
    address = Column(String(256), nullable=False)                                       # Shipment address
    products = relationship('Product', backref='orders', lazy= 'dynamic')               # List of the products that will be shipped
    price = Column(Float(), nullable=False)                                             # Total price of the order

    def __repr__(self):
        return "<Order(%s, %f)>" % (self.address, self.price)

    def toDict(self):
        return {
            "id": self.id,
            "restorant": self.restaurant,
            "adress": self.address,
            "price": self.price
        }
        # Dont send the list of the products because it can be heavy
