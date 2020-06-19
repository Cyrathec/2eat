from model.mapping.product import Product
from model.mapping.restaurant import Restaurant, RestaurantProductAssociation
from model.mapping.order import Order, OrderProductAssociation
from model.dao.dao import DAO
from model.dao.dao_error_handler import dao_error_handler

class ProductDAO(DAO):
	"""
	Product Mapping DAO
	"""

	def __init__(self, database_session):
		super().__init__(database_session)

	@dao_error_handler
	def get(self, id):
		return self._database_session.query(Product).filter_by(id=id).one()

	@dao_error_handler
	def get_all(self):
		return self._database_session.query(Product).order_by(Product.name).all()

	@dao_error_handler
	def get_by_name(self, name):
		return self._database_session.query(Product).filter_by(name=name).one()

	@dao_error_handler
	def create(self, data: dict):
		product = Product(name=data.get('name'), price=float(data.get('price')))
		self._database_session.add(product)
		self._database_session.flush()
		return product

	@dao_error_handler
	def _update_address(self, product, address: str):
		product.set_address(address)

	@dao_error_handler
	def update(self, product: Product, data: dict):
		if 'name' in data:
			product.name = data['name']
		if 'price' in data:
			product.price = data['price']

		self._database_session.merge(product)
		self._database_session.flush()
		return product

	@dao_error_handler
	def delete(self, entity):
		self._database_session.query(RestaurantProductAssociation).filter(RestaurantProductAssociation.Product_id==entity.id).delete()
		self._database_session.query(OrderProductAssociation).filter(OrderProductAssociation.Product_id==entity.id).delete()
		self._database_session.commit()
		self._database_session.delete(entity)
