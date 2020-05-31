from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    # Sport is unique in database
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(512), nullable=True)
    restaurant = relationship("Product", back_populates="products")

    def __repr__(self):
        return "<Sport %s>" % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "Price": self.description
        }


class ProductAssociation(Base):
    """
    Association class between person and sport
    help relationship: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
    """
    __tablename__ = 'product_associations'
    __table_args__ = (UniqueConstraint('restaurant_id', 'product_id'),)

    restaurant_id = Column(String(36), ForeignKey('restaurant.id'), primary_key=True)
    product_id = Column(String(36), ForeignKey('products.id'), primary_key=True)
    restaurant = relationship("Restaurant", back_populates="products")
    product = relationship("Product", back_populates="restaurant")
