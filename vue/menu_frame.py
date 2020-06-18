from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, root_frame,person=None ,isAdmin=False):
        super().__init__(root_frame)
        self._is_admin = isAdmin
        self.person = person
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Welcome in 2eat App")
        self.restaurants = Button(self, text="Restaurants", width=30, command=self._root_frame.show_restaurants)
        self.orders = Button(self, text="Orders", width=30, command=self._root_frame.show_restaurants) # rien n'a été fait à part le bouton, il affiche les restaurants
        self.basket = Button(self, text="Basket", width=30, command=self._root_frame.show_basket)
        if self._is_admin == True :
            self.products = Button(self, text="Products", width=30, command=self._root_frame.show_products)
        
        
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
        self.restaurants.pack()
        self.orders.pack()
        self.basket.pack()
        if self._is_admin == True :
            self.products.pack()
        

        self.quit.pack(side="bottom")
