from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class NewRestaurantFrame(BaseFrame):

    def __init__(self, restaurant_controller, master=None):
        super().__init__(master)
        self.create_widgets()
        self._restaurant_controller = restaurant_controller

    def create_widgets(self):

        Label(self, text="Data informations:", font='bold').grid(row=0, sticky='w')
        self.name_entry = self.create_entry("name", row=1)

        Label(self, text="Address:", font='bold').grid(row=3, sticky='w')
        self.address_entry = self.create_entry("address", row=4)
       
        self.valid = Button(self, text="valid", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="cancel", fg="red",
                             command=self.back)
        self.valid.grid(row=8, column=1, sticky=E)
        self.cancel.grid(row=8, column=2, sticky=W)

    def get_data(self):
        data = dict(name=self.name_entry.get(), address=self.address_entry.get())
        return data

    def valid(self):
        data = self.get_data()
        try:
            restaurant_data = self._restaurant_controller.create_restaurant(data)
            messagebox.showinfo("Success",
                                "Restaurant %s at %s created !" % (restaurant_data['name'], restaurant_data['address']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.back()
