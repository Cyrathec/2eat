from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Produit(Base):
    __tablename__ = 'produits'

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    # Sport is unique in database
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(512), nullable=True)
    restaurant = relationship("Produit", back_populates="produits")

    def __repr__(self):
        return "<Sport %s>" % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "Price": self.description
        }


class ProduitAssociation(Base):
    """
    Association class between person and sport
    help relationship: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
    """
    __tablename__ = 'produit_associations'
    __table_args__ = (UniqueConstraint('restaurant_id', 'produit_id'),)

    restaurant_id = Column(String(36), ForeignKey('restaurant.id'), primary_key=True)
    produit_id = Column(String(36), ForeignKey('produits.id'), primary_key=True)
    restaurant = relationship("Restaurant", back_populates="produits")
    produit = relationship("Produit", back_populates="restaurant")
