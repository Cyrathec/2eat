
from tkinter import *

from vue.base_frame import BaseFrame
from controller.restaurant_controller import RestaurantController


class ListRestaurantsFrame(BaseFrame):

    def __init__(self, restaurant_controller: RestaurantController, root_frame: Frame,isAdmin=None):
        super().__init__(root_frame)
        self._restaurant_controller = restaurant_controller
        self._is_admin = isAdmin
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
        if self._is_admin == True :
            self.new_restaurant_button = Button(self, text="New restaurant", command=self.new_restaurant)
        self.show_profile_button = Button(self, text="Show products", command=self.show_profile)
        self.menu = Button(self, text="Return", fg="red",
                           command=self.show_menu)
        if self._is_admin == True :
            self.new_restaurant_button.grid(row=3, sticky="nsew")
        self.menu.grid(row=4, column=0, sticky="w")

        #TODO copier dans un autre fichier
        """
        self.title = Label(self, text="List %s:" % self._person_type.capitalize())
       
        self.connexion_button = Button(self, text="Connexion", command=self.connexion)
        self.menu = Button(self, text="Return", fg="red",
                           command=self.show_menu)
        self.inscription_button = Button(self, text="Inscription", command=self.inscription)

        self.inscription_button.grid(row=5, sticky="W")
        self.connexion_button.grid(row = 4, sticky="w")
        self.menu.grid(row=6, column=0, sticky="w")
        




    
    
    def connexion(self):
        self._root_frame.connexion_frame()
    """
    def new_restaurant(self):
        self._root_frame.new_restaurant()

    def show_profile(self):
        if len(self.listbox.curselection()) == 0:
            self.show_profile_button.grid_forget()
        else:
            index = int(self.listbox.curselection()[0])
            restaurant = self._restaurants[index]
            self._root_frame.show_products_restaurant(restaurant)

    def show(self):
        self._restaurants = self._restaurant_controller.list_restaurants()
        self.listbox.delete(0, END)
        for index, restaurant in enumerate(self._restaurants):
            text = restaurant['name'] + ', ' + restaurant['address']
            self.listbox.insert(index, text)
        super().show()

    def on_select(self, event):
        if len(self.listbox.curselection()) == 0:
            self.show_profile_button.grid_forget()
        else:
            self.show_profile_button.grid(row=3, column=1, sticky="nsew")
    """TODO copier dans un autre fichier
    def new_person(self):
        if self._person_type == 'member':
            self._root_frame.new_member()
 
    def inscription(self):
        self._root_frame.new_member()
    

    def show(self):
        
    """
            
