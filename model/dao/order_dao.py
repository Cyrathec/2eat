from model.mapping.order import Order
from model.dao.dao import DAO
from model.dao.dao_error_handler import dao_error_handler

from model.mapping.product import Product


class OrderDAO(DAO):
	"""
	Order Mapping DAO
	"""

	# Get a specific order by its id
	@dao_error_handler
	def get(self, id):
		return self._database_session.query(Order).filter_by(id=id).one()

	# Get all orders ordered by their client
	@dao_error_handler
	def getAll(self):
		return self._database_session.query(Order).order_by(Order.client).all()

	# Get all orders from a specific client
	@dao_error_handler
	def getByClient(self, client: str):
		return self._database_session.query(Order).filter_by(client=client).order_by(Order.id).all()

	# Get all orders from a specific restaurant
	@dao_error_handler
	def getByRestaurant(self, restaurant: str):
		return self._database_session.query(Order).filter_by(restaurant=restaurant).order_by(Order.id).all()

	# Create an order
	@dao_error_handler
	def create(self, data: dict):
		order = Order(client=data.get('client'), restaurant=data.get('restaurant'), address=data.get('address'), price=0.0)
		self._database_session.add(order)
		for product in data['products']:
			product_obj = self._database_session.query(Product).filter_by(id=product['id']).one()
			order.add_product(product_obj, self._database_session)
		self._database_session.flush()
		return order

####################################################################################################################################################
#####                                                           Illogics functions                                                             #####
#####                                               A order shouldn't be updated or deleted                                                    #####
####################################################################################################################################################

	# Update an order
	@dao_error_handler
	def update(self, order: Order, data: dict):
		if 'restaurant' in data:
			order.restaurant = data['restaurant']
		if 'address' in data:
			order.address = data['address']
		if 'products' in data:
			order.price = 0
			order.products.clear()
			for product in data['products']:
				order.products.append(product)
				order.price += product['price']
				
		self._database_session.merge(order)
		self._database_session.flush()

		return order

	# Delete an order
	@dao_error_handler
	def delete(self, entity):
		self._database_session.delete(entity)
