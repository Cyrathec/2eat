
from model.dao.restaurant_dao import RestaurantDAO




class PersonDAOFabric:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_dao(self, type=None):
        if type is None:
            return RestaurantDAO(self._database_session)
        if type == "restaurant":
            return RestaurantDAO(self._database_session)
        else:
             return RestaurantDAO(self._database_session)
    