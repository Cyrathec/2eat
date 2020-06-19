import re
import logging

from model.basket import Basket

from exceptions import Error, InvalidData

class BasketController:
    """
    Order actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self.numberofbaskets = 0
        self.baskets = []

    def getBasket(self, id):
        if id < len(self.baskets) :
            return self.baskets[id].toDict()
        else :
            return []

    def listBaskets(self):
        baskets = [basket.toDict() for basket in self.baskets]
        return baskets
    
    def createBasket(self, restaurant, client, address):
        basket = Basket(self.numberofbaskets, restaurant, client, address)
        self.numberofbaskets += 1
        self.baskets.append(basket)
        return basket.toDict()

    def delBasket(self, id):
        basket = self.baskets[id].toDict()
        del self.baskets[id]
        self.numberofbaskets -= 1
        return basket

    def addProduct(self, id, product):
        self.baskets[id].addProduct(product)
        return self.baskets[id].toDict()

    def delProduct(self, id, product):
        if type(product) is int:
            self.baskets[id].delProductAtIndex(product)
        else:
            self.baskets[id].delProduct(product)
        return self.baskets[id].toDict()

    def updateRestaurant(self, id, restaurant):
        self.baskets[id].updateRestaurant(restaurant)
        return self.baskets[id].toDict()

    def updateAddress(self, id, address):
        self.baskets[id].updateAddress(address)
        return self.baskets[id].toDict()