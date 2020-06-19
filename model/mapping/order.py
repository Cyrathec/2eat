from model.mapping import Base
import uuid
from model.mapping.product import Product
from model.mapping.restaurant import Restaurant
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class OrderProductAssociation(Base):
	__tablename__ = 'OrderProductAssociation'

	id = Column(Integer, primary_key=True)

	Order_id = Column(Integer, ForeignKey('Order.id'))
	Product_id = Column(Integer, ForeignKey('Product.id'))

	product = relationship("Product")


class Order(Base):
	__tablename__ = 'Order'

	id = Column(Integer, primary_key=True)

	restaurant = Column(Integer, ForeignKey('Restaurant.id'))                                       # ForeignKey to the Restaurant id
	client = Column(String(36), ForeignKey('Person.id'))                                            # ForeignKey to the client id
	address = Column(String(512), nullable=False)                                                   # Shipment address
	products = relationship("OrderProductAssociation")                                              # List of the products that will be shipped
	price = Column(Float(), nullable=False)                                                         # Total price of the order

	def __repr__(self):
		return "<Order(%d, %s, %f)>" % (self.id, self.address, self.price)

	def toDict(self):
		products = []
		for product_association in self.products:
			products.append({
				"id": product_association.product.id,
				"name": product_association.product.name,
				"price": product_association.product.price
			})
		return {
			"id": self.id,
			"restaurant": self.restaurant,
			"client": self.client,
			"address": self.address,
			"products": products,
			"price": self.price
		}

	def add_product(self, product, session):
		asociation = OrderProductAssociation()
		asociation.product = product
		self.products.append(asociation)
		self.price += product.price
		self.price = round(self.price, 2)
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
			self.price -= product.price
			self.price = round(self.price, 2)
			session.flush()