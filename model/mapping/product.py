from model.mapping import Base
import uuid

from sqlalchemy import Column, Integer, String, Float, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True)

    # Sport is unique in database
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return "<Product %s %0.2f>" % (self.name, self.price)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }
