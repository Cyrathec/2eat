import re
import logging

from model.dao.product_dao import ProductDAO

from exceptions import Error, InvalidData


class ProductController:
    """
    Product actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_products(self):
        logging.info("List products")
        with self._database_engine.new_session() as session:
            products = ProductDAO(session).get_all()
            products_data = [product.to_dict() for product in products]
        return products_data

    def get_product(self, product_id):
        logging.info("Get product %s" % product_id)
        with self._database_engine.new_session() as session:
            product = ProductDAO(session).get(product_id)
            product_data = product.to_dict()
        return product_data

    def create_product(self, data):
        logging.info("Create product with data %s" % str(data))
        self._check_product_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save product in database
                dao = ProductDAO(session)
                product = dao.create(data)
                product_data = product.to_dict()
                return product_data
        except Error as e:
            # log error
            logging.error("An Error occured (%s)" % str(e))
            raise e

    def update_product(self, product_id, product_data):
        logging.info("Update product %s with data: %s" % (product_id, str(product_data)))
        with self._database_engine.new_session() as session:
            dao = ProductDAO(session)
            product = dao.get(product_id)
            product = dao.update(product, product_data)
            return product.to_dict()

    def delete_product(self, product_id):
        logging.info("Delete product %s" % product_id)
        with self._database_engine.new_session() as session:
            dao = ProductDAO(session)
            product = dao.get(product_id)
            dao.delete(product)

    def search_product(self, name):
        logging.info("Search product %s" % name)
        # Query database
        with self._database_engine.new_session() as session:
            dao = ProductDAO(session)
            product = dao.get_by_name(name)
            return product.to_dict()

    def _check_product_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        specs = {
            "name": {"type": str, "regex": name_pattern},
            "price": {"type": float}
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