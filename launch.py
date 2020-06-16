from controller.order_controller import OrderController
from controller.basket_controller import BasketController
from model.database import DatabaseEngine

database_engine = DatabaseEngine(url='sqlite:///database.db')
database_engine.create_database()

restaurant = 1
client = 1
address = "104 Avenue Pierre de Coubertin"

basketController = BasketController(database_engine)
orderController = OrderController(database_engine)

product1 = {'id':1, 'name':"BigMac", 'price': 3.49}
product2 = {'id':2, 'name':"Frites", 'price': 1.0}
product3 = {'id':3, 'name':"Bucket", 'price': 8.95}
product4 = {'id':4, 'name':"Coca", 'price': 1.0}
product5 = {'id':5, 'name':"Kebab", 'price': 3.0}
product6 = {'id':6, 'name':"Whopper", 'price': 3.49}
product7 = {'id':7, 'name':"Sundae", 'price': 3.0}