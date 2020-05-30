from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Welcome ")
      
        self.restaurant = Button(self, text="restaurant", width=30, command=self._root_frame.show_members)
      
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
       
        self.restaurant.pack()
        self.quit.pack(side="bottom")
