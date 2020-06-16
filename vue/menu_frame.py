from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, root_frame, isAdmin=False):
        super().__init__(root_frame)
        self._is_admin = isAdmin
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Welcome in 2eat App")
        self.restaurants = Button(self, text="Restaurants", width=30, command=self._root_frame.show_restaurants)
        if self._is_admin == True :
            self.products = Button(self, text="Products", width=30, command=self._root_frame.show_products)
        self.members = Button(self, text="Members", width=30, command=self._root_frame.show_members)
        
        
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
        self.members.pack()
        self.restaurants.pack()
        if self._is_admin == True :
            self.products.pack()
        #TODO

        self.quit.pack(side="bottom")
