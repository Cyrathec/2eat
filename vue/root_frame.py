from tkinter import *

from vue.menu_frame import MenuFrame

from vue.restaurant_frames.list_restaurant_frame import ListRestaurantsFrame
from vue.restaurant_frames.new_restaurant_frame import NewRestaurantFrame
from vue.restaurant_frames.profile_frame import ProfileFrame

from vue.product_frames.list_products_frame import ListProductsFrame
from vue.product_frames.new_product_frame import NewProductFrame
from vue.product_frames.product_profile_frame import ProductProfileFrame
from vue.person_frames.new_person_frame import NewPersonFrame
from vue.person_frames.list_persons_frame import ListPersonsFrame
from vue.person_frames.person_profile_frame import PersonProfileFrame
from vue.auth_portal import AuthPortal

from vue.basket_frames.basket_frame import BasketFrame

from vue.connexion_frame import ConnexionFrame


class RootFrame(Frame):
    """
    Member actions
    help: http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html
    """

    def __init__(self, restaurant_controller, product_controller, person_controller, basket_controller, order_controller, master=None):
        super().__init__(master)
        self._restaurant_controller = restaurant_controller
        self._product_controller = product_controller
        self._person_controller = person_controller
        self._basket_controller = basket_controller
        self._order_controller = order_controller
        self._menu_frame = []
        self._frames = []

        self._user = None

    def new_restaurant(self):
        self.hide_frames()
        # Show formular restaurant
        new_restaurant_frame = NewRestaurantFrame(self._restaurant_controller, self)
        new_restaurant_frame.show()
        self._frames.append(new_restaurant_frame)

    def new_product(self):
        self.hide_frames()
        new_product_frame = NewProductFrame(self._product_controller, self)
        new_product_frame.show()
        self._frames.append(new_product_frame)

    def new_member(self):
        self.hide_frames()
        # Show formular subscribe
        subscribe_frame = NewPersonFrame(self._person_controller, self)
        subscribe_frame.show()
        self._frames.append(subscribe_frame)

    def show_restaurants(self):
        # show restaurants
        self.hide_menu()
        list_frame = ListRestaurantsFrame(self._restaurant_controller, self, isAdmin=self._user.get("isAdmin"))
        self._frames.append(list_frame)
        list_frame.show()

    def show_restaurant(self, restaurant_id):
        restaurant_data = self._restaurant_controller.get_restaurant(restaurant_id)

        self.hide_frames()
        profile_frame = ProfileFrame(self._restaurant_controller, self._product_controller, restaurant_data, self)
        self._frames.append(profile_frame)
        profile_frame.show()

    def show_products(self):
        self.hide_menu()
        list_frame = ListProductsFrame(self._product_controller, self, isAdmin=self._user.get("isAdmin"))
        self._frames.append(list_frame)
        list_frame.show()

    def show_products_restaurant(self, restaurant_id):
        restaurant_data = self._restaurant_controller.get_restaurant(restaurant_id)

        self.hide_frames()
        list_frame = ListProductsFrame(self._product_controller, self, restaurant_data, isAdmin=self._user.get("isAdmin"))
        self._frames.append(list_frame)
        list_frame.show()

    def show_product(self, product_id):
        product_data = self._product_controller.get_product(product_id)

        self.hide_frames()
        profile_frame = ProductProfileFrame(self._product_controller, product_data, self, isAdmin=self._user.get("isAdmin"))
        self._frames.append(profile_frame)
        profile_frame.show()

    def show_basket(self):
        self.hide_menu()
        basket_frame = BasketFrame(self._basket_controller, self)
        self._frames.append(basket_frame)
        basket_frame.show()

    def add_to_basket(self, product_id, restaurant_id):
        product_data = self._product_controller.get_product(product_id)
        if self._basket_controller.getBasket(0) != []:
            self._basket_controller.addProduct(0, product_data)
        else:
            basket = self._basket_controller.createBasket(restaurant_id, self._user['id'], self._user['address'])
            self._basket_controller.addProduct(basket['id'], product_data)

    def order_basket(self, basket):
        order_frame = order_frame(self._order_controller, self)
        self._order_controller
        
    def show_person(self, person_id, editable=False):
        person_data = self._person_controller.get_person(person_id)

        self.hide_menu()
        self.hide_frames()
        profile_frame = PersonProfileFrame(self._person_controller, person_data, self, editable)
        self._frames.append(profile_frame)
        profile_frame.show()
    
    def show_persons(self):
        self.hide_menu()
        list_frame = ListPersonsFrame(self._person_controller, self, display_admins_only=None)
        self._frames.append(list_frame)
        list_frame.show()

    def show_auth_portal(self):
        self._user = None
        auth_frame = AuthPortal(self._person_controller, self, person_type='member')
        self._frames.append(auth_frame)
        auth_frame.show()

    def connexion_frame(self):
       #connexion
       self.hide_frames()
       connexion_frame = ConnexionFrame(self._person_controller, self)
       self._frames.append(connexion_frame)
       connexion_frame.show()

    def hide_frames(self):
        for frame in self._frames:
            frame.hide()

    def show_menu(self,member=None):

        if self._user is None and member is not None:
            self._user = member

        for frame in self._frames:
            frame.destroy()
        self._menu_frame = MenuFrame(self,self._user, self._user.get("isAdmin"))
        self._frames = []
        self._menu_frame.show()

    def hide_menu(self):
        self._menu_frame.hide()

    def back(self):
        if len(self._frames) <= 1:
            self.show_menu()
            return
        last_frame = self._frames[-1]
        last_frame.destroy()
        del(self._frames[-1])
        last_frame = self._frames[-1]
        last_frame.show()

    def cancel(self):
        self.show_menu()

    def quit(self):
        self.master.destroy()
