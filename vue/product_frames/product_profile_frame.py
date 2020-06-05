from tkinter import *
from tkinter import messagebox

from vue.product_frames.product_formular_frame import ProductFormularFrame
from exceptions import Error


class ProductProfileFrame(ProductFormularFrame):

	def __init__(self, product_controller, product, master=None):
		super().__init__(master)
		self._product_controller = product_controller
		self._product = product
		self.refresh()

	def create_widgets(self):
		super().create_widgets()

		# Buttons
		self.edit_button = Button(self, text="Edit",
								  command=self.edit)
		self.cancel_button = Button(self, text="Cancel", command=self.refresh)
		self.update_button = Button(self, text="Update", command=self.update)
		self.remove_button = Button(self, text="Remove", command=self.remove)
		self.return_button = Button(self, text="Return", fg="red",
									command=self.back)

		self.return_button.grid(row=20, column=0)
		self.edit_button.grid(row=20, column=1, sticky="nsew")
		self.remove_button.grid(row=20, column=2, sticky="nsew")

	def edit(self):
		self.edit_button.grid_forget()
		self.remove_button.grid_forget()
		entries = [self.name_entry, self.price_entry]
		for entry in entries:
			entry.config(state=NORMAL)

		# remove '€' at the end of price_entry
		self.price_entry.delete(0, END)
		self.price_entry.insert(0, str(self._product['price']))

		self.cancel_button.grid(row=20, column=2, sticky="nsew")
		self.update_button.grid(row=20, column=1, sticky="nsew")

	def _refresh_entry(self, entry, value=""):
		entry.delete(0, END)
		if value != "":
			entry.insert(0, value)
		entry.config(state=DISABLED)

	def refresh(self):
		# Restore window with product value and cancel edition
		self.cancel_button.grid_forget()
		self.update_button.grid_forget()
		self._refresh_entry(self.name_entry, self._product['name'])
		self._refresh_entry(self.price_entry, str(self._product['price']) + "€")
		self.edit_button.grid(row=20, column=1, sticky="nsew")
		self.remove_button.grid(row=20, column=2, sticky="nsew")

	def update(self):

		data = self.get_data()
		product = self._product_controller.update_product(self._product['id'], data)
		self._product = product
		self.refresh()

	def remove(self):
		product_id = self._product['id']
		self._product_controller.delete_product(product_id)
		# show confirmation
		messagebox.showinfo("Success",
							"Product %s deleted !" % self._product['name'])
		self.back()