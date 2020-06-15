
from tkinter import *

from vue.base_frame import BaseFrame
from controller.person_controller import PersonController


class ListMembersFrame(BaseFrame):

    def __init__(self, person_controller: PersonController, root_frame: Frame, person_type: str = None):
        super().__init__(root_frame)
        self._person_controller = person_controller

        self._members = None
        if person_type is None:
            self._person_type = 'person'
        else:
            self._person_type = person_type
        self._create_widgets()

    def _create_widgets(self):

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

    def new_person(self):
        if self._person_type == 'member':
            self._root_frame.new_member()
 
    def inscription(self):
        self._root_frame.new_member()
    

    def show(self):
        
        
            
        super().show()
