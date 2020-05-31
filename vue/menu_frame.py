from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Welcome in 2eat App")
        self.restaurants = Button(self, text="Restaurants", width=30, command=self._root_frame.show_restaurants)
        self.products = Button(self, text="Products", width=30, command=self._root_frame.show_products)
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
        
        self.restaurants.pack()
        self.products.pack()
        self.quit.pack(side="bottom")
