from model.mapping.product import Product
from model.dao.dao import DAO
from model.dao.dao_error_handler import dao_error_handler


class ProductDAO(DAO):
    """
    Sport Mapping DAO
    """

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(Product).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self):
        return self._database_session.query(Product).order_by(Product.name).all()

    @dao_error_handler
    def get_by_name(self, name: str):
        return self._database_session.query(Product).filter_by(name=name).one()

    @dao_error_handler
    def create(self, data: dict):
        product = Product(name=data.get('name'), description=data.get('description'))
        self._database_session.add(product)
        self._database_session.flush()
        return product

    @dao_error_handler
    def update(self, sport: Product, data: dict):
        if 'name' in data:
            sport.name = data['name']
        if 'description' in data:
            sport.description = data['description']

        self._database_session.merge(sport)
        self._database_session.flush()

        return sport

    @dao_error_handler
    def delete(self, entity):
        self._database_session.delete(entity)
