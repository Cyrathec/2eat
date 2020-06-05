import re
import logging

from model.dao.restaurant_dao import RestaurantDAO
from model.dao.product_dao import ProductDAO

from exceptions import Error, InvalidData

class RestaurantController:
	"""
	Restaurant actions
	"""

	def __init__(self, database_engine):
		self._database_engine = database_engine

	def list_restaurants(self):
		logging.info("Get restaurants")
		with self._database_engine.new_session() as session:
			dao = RestaurantDAO(session)
			restaurants = dao.get_all()
			restaurants_data = [restaurant.to_dict() for restaurant in restaurants]
		return restaurants_data

	def get_restaurant(self, restaurant_id):
		logging.info("Get restaurant %s" % restaurant_id)
		with self._database_engine.new_session() as session:
			dao = RestaurantDAO(session)
			restaurant = dao.get(restaurant_id)
			restaurant_data = restaurant.to_dict()
		return restaurant_data

	def create_restaurant(self, data):
		logging.info("Create restaurant with data %s" % str(data))
		self._check_restaurant_data(data)
		try:
			with self._database_engine.new_session() as session:
				# Save member in database
				dao = RestaurantDAO(session)
				restaurant = dao.create(data)
				restaurant_data = restaurant.to_dict()
				return restaurant_data
		except Error as e:
			# log error
			logging.error("An Error occured (%s)" % str(e))
			raise e

	def _update_restaurant(self, restaurant_id, restaurant_data):
		logging.info("Update restaurant %s with data: %s" % (restaurant_id, str(restaurant_data)))
		with self._database_engine.new_session() as session:
			dao = RestaurantDAO(session)
			restaurant = dao.get(restaurant_id)

			restaurant = dao.update(restaurant, restaurant_data)
			return restaurant.to_dict()

	def update_restaurant(self, restaurant_id, restaurant_data):
		self._check_restaurant_data(restaurant_data, update=True)
		return self._update_restaurant(restaurant_id, restaurant_data)
	
	def add_product_restaurant(self, restaurant_id, product_id):
		logging.info("Add product %s to restaurant %s" % (product_id, restaurant_id))
		with self._database_engine.new_session() as session:
			restaurant = RestaurantDAO(session).get(restaurant_id)
			product = ProductDAO(session).get(product_id)
			restaurant.add_product(product, session)
			return restaurant.to_dict()

	def delete_product_restaurant(self, restaurant_id, product_id):
		logging.info("Delete product %s from restaurant %s" % (product_id, restaurant_id))
		with self._database_engine.new_session() as session:
			restaurant = RestaurantDAO(session).get(restaurant_id)
			product = ProductDAO(session).get(product_id)
			restaurant.delete_product(product, session)
			return restaurant.to_dict()
	
	def delete_restaurant(self, restaurant_id):
		logging.info("Delete restaurant %s" % restaurant_id)
		with self._database_engine.new_session() as session:
			dao = RestaurantDAO(session)
			restaurant = dao.get(restaurant_id)
			dao.delete(restaurant)

	def _check_restaurant_data(self, data, update=False):
		
		specs = {
			'name': {"type": str},
			'address': {"type": str}
		}
		self._check_data(data, specs, update=update)

	def _check_data(self, data, specs, update=False):
		for mandatory, specs in specs.items():
			if not update:
				if mandatory not in data or data[mandatory] is None:
					raise InvalidData("Missing value %s" % mandatory)
			else:
				if mandatory not in data:
					continue
			value = data[mandatory]
			if "type" in specs and not isinstance(value, specs["type"]):
				raise InvalidData("Invalid type %s" % mandatory)
			if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
				raise InvalidData("Invalid value %s" % mandatory)