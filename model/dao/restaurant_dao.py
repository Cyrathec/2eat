from model.mapping.restaurant import Restaurant
from model.dao.dao import DAO
from model.dao.dao_error_handler import dao_error_handler

class RestaurantDAO(DAO):
	"""
	Restaurant Mapping DAO
	"""

	def __init__(self, database_session):
		super().__init__(database_session)

	@dao_error_handler
	def get(self, id):
		return self._database_session.query(Restaurant).filter_by(id=id).one()

	@dao_error_handler
	def get_all(self):
		return self._database_session.query(Restaurant).order_by(Restaurant.name).all()

	@dao_error_handler
	def get_by_name(self, name):
		return self._database_session.query(Restaurant).filter_by(name=name).one()

	@dao_error_handler
	def create(self, data: dict):
		restaurant = Restaurant(name=data.get('name'), address=data.get('address'))
		self._database_session.add(restaurant)
		self._database_session.flush()
		return restaurant

	@dao_error_handler
	def _update_address(self, restaurant, address):
		restaurant.address = address

	@dao_error_handler
	def update(self, restaurant: Restaurant, data: dict):
		if 'name' in data:
			restaurant.name = data['name']
		if 'address' in data:
			self._update_address(restaurant, data['address'])

		self._database_session.merge(restaurant)
		self._database_session.flush()
		return restaurant

	@dao_error_handler
	def delete(self, entity):
		self._database_session.delete(entity)