from tkinter import *
from tkinter import messagebox

from vue.product_frames.product_formular_frame import ProductFormularFrame
from exceptions import Error


class NewProductFrame(ProductFormularFrame):

    def __init__(self, product_controller, master=None):
        super().__init__(master)
        self._product_controller = product_controller

    def create_widgets(self):
        super().create_widgets()
        self.valid = Button(self, text="valid", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="cancel", fg="red",
                             command=self.back)
        self.valid.grid(row=20, column=1, sticky=E)
        self.cancel.grid(row=20, column=2, sticky=W)

    def valid(self):
        data = self.get_data()
        try:
            product_data = self._product_controller.create_product(data)
            messagebox.showinfo("Success", "Product %s created !" % product_data['name'])

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.back()
