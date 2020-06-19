from model.mapping import Base
import uuid

from sqlalchemy import Table, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

class RestaurantProductAssociation(Base):
	"""
	Association class between Restaurant and Product
	help relationship: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
	"""
	__tablename__ = 'RestaurantProductAssociation'
	__table_args__ = (UniqueConstraint('Restaurant_id', 'Product_id'),)

	Restaurant_id = Column(Integer, ForeignKey('Restaurant.id'), primary_key=True)
	Product_id = Column(Integer, ForeignKey('Product.id'), primary_key=True)

	product = relationship("Product")

class Restaurant(Base):
	__tablename__ = 'Restaurant'

	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	address = Column(String(512), nullable=False)
	products = relationship("RestaurantProductAssociation", cascade="all, delete-orphan")

	def __repr__(self):
		return "<Restaurant(%s %s)>" % (self.name, self.adress)

	def to_dict(self):
		_data = {
			"id": self.id,
			"name": self.name,
			"address": self.address,
			"products": []
		}

		for product_association in self.products:
			_data['products'].append({"id": product_association.product.id,
									"name": product_association.product.name,
									"price": product_association.product.price})
		
		return _data

	def add_product(self, product, session):
		asociation = RestaurantProductAssociation()
		asociation.product = product
		self.products.append(asociation)
		session.flush()

	def delete_product(self, product, session):
		product_association = None
		for association in self.products:
			if association.product == product:
				product_association = association
				break
		if product_association is not None:
			self.products.remove(product_association)
			session.delete(product_association)
			session.flush()