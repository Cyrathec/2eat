import re
import logging

from model.basket import Basket

from exceptions import Error, InvalidData

class BasketController(DAO):
    """
    Order actions
    """

    def __init__(self):
        self.numberofbaskets = 0
        self.baskets = {}

    def getBasket(self, id):
        return self.basket[id].toDict()

    def listBaskets(self):
        baskets = [basket.toDict() for backet in self.baskets]
        return baskets
    
    def createBasket(self, restaurant, client, address):
        basket = Basket(self.numberofbaskets, restaurant, client, address)
        self.numberofbaskets += 1
        self.baskets.append(basket)
        return basket.toDict()

    def delBasket(self, id):
        basket = self.baskets[id].toDict()
        del self.baskets[id]
        return basket

    def addProduct(self, id, product):
        self.baskets[id].addProduct(product)
        return self.basket[id].toDict()

    def delProduct(self, id, product):
        self.basket[id].delProduct(product)
        return self.basket[id].toDict()

    def updateRestaurant(self, id, restaurant):
        self.baskets[id].updateRestaurant(restaurant)
        return self.basket[id].toDict()

    def updateAddress(self, address):
        self.baskets[id].updateAddress(address)
        return self.basket[id].toDict()