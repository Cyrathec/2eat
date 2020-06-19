
from tkinter import *

from vue.base_frame import BaseFrame
from controller.restaurant_controller import RestaurantController


class RestaurantBasketFrame(BaseFrame):

    def __init__(self, restaurant_controller: RestaurantController, root_frame: Frame):
        super().__init__(root_frame)
        self._restaurant_controller = restaurant_controller
        self._restaurants = None
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="List restaurants:")
        self.title.grid(row=0, column=0)

        # grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        yDefil.grid(row=1, column=2, sticky='ns')
        self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # Return bouton
        self.choose_restaurant_button = Button(self, text="Choose restaurant", command=self.choose_restaurant)

        self.menu = Button(self, text="Return", fg="red",
                           command=self.show_menu)
        self.hide()
        self.menu.grid(row=4, column=0, sticky="w")

    def choose_restaurant(self):
        if len(self.listbox.curselection()) == 0:
            self.choose_restaurant_button.grid_forget()
        else:
            index = int(self.listbox.curselection()[0])
            restaurant = self._restaurants[index]
            self._root_frame.choose_restaurant_basket(restaurant["id"])

    def show(self):
        self._restaurants = self._restaurant_controller.list_restaurants()
        self.listbox.delete(0, END)
        for index, restaurant in enumerate(self._restaurants):
            text = restaurant['name'] + ', ' + restaurant['address']
            self.listbox.insert(index, text)
        super().show()

    def on_select(self, event):
        if len(self.listbox.curselection()) == 0:
            self.choose_restaurant_button.grid_forget()
        else:
            self.choose_restaurant_button.grid(row=3, column=1, sticky="nsew")
            
