import re
import logging

from model.dao.order_dao import OrderDAO

from exceptions import Error, InvalidData

class OrderController:
    """
    Order actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    # List all orders
    def listOrders(self):
        logging.info("List orders")
        with self._database_engine.new_session() as session:
            orders = OrderDAO(session).getAll()
            orders_data = [order.toDict() for order in orders]
        return orders_data

    # Get a specific order by its id
    def getOrder(self, order_id):
        logging.info("Get order %s" % order_id)
        with self._database_engine.new_session() as session:
            order = OrderDAO(session).get(order_id)
            order_data = order.toDict()
        return order_data

    # Create an order with the data that should be a basket
    def createOrder(self, data):
        logging.info("Create order with data %s" % str(data))
        try:
            with self._database_engine.new_session() as session:
                # Save order in database
                dao = OrderDAO(session)
                order = dao.create(data)
                order_data = order.toDict()
                return order_data
        except Error as e:
            # log error
            logging.error("An Error occured (%s)" % str(e))
            raise e

    # Search all orders from a specific client
    def searchOrdersByClient(self, client):
        logging.info("Search orders of %s" % client)
        # Query database
        with self._database_engine.new_session() as session:
            dao = OrderDAO(session)
            orders = dao.getByClient(client)
            orders_data = [order.toDict() for order in orders]
            return orders_data

    def searchOrdersByRestaurant(self, restaurant):
        logging.info("Search orders of %s" % restaurant)
        # Query database
        with self._database_engine.new_session() as session:
            dao = OrderDAO(session)
            orders = dao.getByRestaurant(restaurant)
            orders_data = [order.toDict() for order in orders]
            return orders_data

####################################################################################################################################################
#####                                                           Illogics functions                                                             #####
#####                                               A order shouldn't be updated or deleted                                                    #####
####################################################################################################################################################

    # Update a specific order by its id. data can contain: the address for the shippement, the restaurant id,
    # the client id and a list of products (all the products will be deleted before adding this list)
    def updateOrder(self, order_id, order_data):
        logging.info("Update order %s with data: %s" % (order_id, str(order_data)))
        with self._database_engine.new_session() as session:
            dao = OrderDAO(session)
            order = dao.get(order_id)
            order = dao.update(order, order_data)
            return order.toDict()

    # Delete a specific order by its id
    def deleteOrder(self, order_id):
        logging.info("Delete person %s" % order_id)
        with self._database_engine.new_session() as session:
            dao = OrderDAO(session)
            order = dao.get(order_id)
            dao.delete(order)
