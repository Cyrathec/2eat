
from tkinter import *

from vue.base_frame import BaseFrame
from controller.person_controller import PersonController


class ListRestaurantFrame(BaseFrame):

    def __init__(self, person_controller: PersonController, root_frame: Frame, person_type: str = None):
        super().__init__(root_frame)
        self._person_controller = person_controller

        self._restaurants = None
        if person_type is None:
            self._person_type = 'restaurant'
        else:
            self._person_type = person_type
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="List %s:" % self._person_type.capitalize())
        self.title.grid(row=0, column=0)

        # grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        yDefil.grid(row=1, column=2, sticky='ns')
        self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # Return bouton
       
        self.show_profile_button = Button(self, text="Show restaurant", command=self.show_profile)
        self.menu = Button(self, text="Return", fg="red",
                           command=self.show_menu)
        
        self.menu.grid(row=4, column=0, sticky="w")

    def on_select(self, event):
        if len(self.listbox.curselection()) == 0:
            self.show_profile_button.grid_forget()
        else:
            self.show_profile_button.grid(row=3, column=1, sticky="nsew")


    def show_profile(self):
        if len(self.listbox.curselection()) == 0:
            self.show_profile_button.grid_forget()
        else:
            index = int(self.listbox.curselection()[0])
            restaurant = self._restaurants[index]
            self._root_frame.show_profile(restaurant['id'])

    def show(self):
        self._restaurants = self._person_controller.list_people(person_type=self._person_type)
        self.listbox.delete(0, END)
        for index, member in enumerate(self._restaurants):
            text = member['restaurant_name'].capitalize() 
            self.listbox.insert(index, text)
        super().show()
