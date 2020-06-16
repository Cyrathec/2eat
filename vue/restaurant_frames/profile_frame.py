
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from vue.base_frame import BaseFrame
from functools import partial

class ProfileFrame(BaseFrame):

	def __init__(self, restaurant_controller, product_controller, restaurant, master=None):
		super().__init__(master)
		self._restaurant = restaurant
		print(self._restaurant)
		self._restaurant_controller = restaurant_controller
		self._product_controller = product_controller
		self._products = []
		self._create_widgets()
		

	def _create_widgets(self):

		self.title = Label(self, text="Restaurant profile: ", font='bold')
		self.title.grid(row=0, column=0, sticky=W)

		self.name_entry = self.create_entry("Name: ", row=1, columnspan=3)

		Label(self, text="Address:", font='bold').grid(row=3, sticky='w')
		self.address_entry = self.create_entry("Address: ", row=4, columnspan=5)

		# Buttons
		self.edit_button = Button(self, text="Edit", command=self.edit)
		self.cancel_button = Button(self, text="Cancel", command=self.refresh)
		self.update_button = Button(self, text="Update", command=self.update)
		self.remove_button = Button(self, text="Remove", command=self.remove)
		self.return_button = Button(self, text="Return", fg="red", command=self.back)

		self.return_button.grid(row=8, column=0)
		self.edit_button.grid(row=8, column=1, sticky="nsew")
		self.remove_button.grid(row=8, column=2, sticky="nsew")

		# Product Frame
		self.products_frame = Frame(self)
		self.products_frame.grid(row=0, column=6, rowspan=20, sticky="n", padx=10)
		self.list_products_frame = None

	def edit(self):
		self.edit_button.grid_forget()
		self.remove_button.grid_forget()
		entries = [self.name_entry, self.address_entry]
		for entry in entries:
			entry.config(state=NORMAL)
		self.cancel_button.grid(row=8, column=2, sticky="nsew")
		self.update_button.grid(row=8, column=1, sticky="nsew")

	def _refresh_entry(self, entry, value=""):
		entry.delete(0, END)
		if value != "":
			entry.insert(0, value)
		entry.config(state=DISABLED)

	def refresh(self):
		# Restore window with person value and cancel edition
		self.cancel_button.grid_forget()
		self.update_button.grid_forget()
		self._refresh_entry(self.name_entry, self._restaurant['name'])
		self._refresh_entry(self.address_entry, self._restaurant['address'])
		self.edit_button.grid(row=8, column=1, sticky="nsew")
		self.remove_button.grid(row=8, column=2, sticky="nsew")
		self.refresh_products()

	def refresh_products(self):

		if self.list_products_frame is not None:
			self.list_products_frame.destroy()
		self.list_products_frame = Frame(master=self.products_frame)
		self.list_products_frame.grid(row=1, columnspan=3, sticky="w")

		Label(self.list_products_frame, text="Products: ", font='bold').grid(row=0, sticky="w")
		i = 1
		if "products" in self._restaurant:
			for product in self._restaurant['products']:
				self.list_products_frame.columnconfigure(i, weight=1)
				Label(self.list_products_frame, text=product['name']).grid(row=i, column=0, sticky="w")
				Label(self.list_products_frame, text=product['price']).grid(row=i, column=1, sticky="w")
				del_button = Button(self.list_products_frame, text="-", command=partial(self.delete_product, product['id']))
				del_button.grid(row=i, column=2, sticky="w")
				i += 1

		# Add product
		self.choose_product_box = ttk.Combobox(self.list_products_frame, values=[product['name'] for product in self._products])
		self.add_product_button = Button(self.list_products_frame, text="+", command=self.add_product)

		self.choose_product_box.grid(row=i, column=0, stick="nsew")
		self.add_product_button.grid(row=i, column=2, stick="w")

	def update(self):

		data = dict(name=self.name_entry.get(), address=self.address_entry.get())

		restaurant = self._restaurant_controller.update_restaurant(self._restaurant['id'], data)
		self._restaurant = restaurant
		self.refresh()

	def remove(self):
		restaurant_id = self._restaurant['id']
		self._restaurant_controller.delete_restaurant(restaurant_id)
		# show confirmation
		messagebox.showinfo("Success",
							"restaurant %s at %s deleted !" % (self._restaurant['name'], self._restaurant['address']))
		self.back()

	def get_product_id(self, name):
		for product in self._products:
			if product['name'] == name:
				return product['id']
		return None

	def add_product(self):
	    product_name = self.choose_product_box.get()
	    if product_name != "":
	        product_id = self.get_product_id(product_name)
	        if product_id is not None:
	            self._restaurant = self._restaurant_controller.add_product_restaurant(self._restaurant['id'], product_id)
	        else:
	            messagebox.showerror("Product %s not found" % product_name)
	    self.refresh_products()

	def delete_product(self, product_id):
		self._restaurant = self._restaurant_controller.delete_product_restaurant(self._restaurant['id'], product_id)
		self.refresh_products()

	def show(self):
		self._products = self._product_controller.list_products()
		self.refresh()
		super().show()