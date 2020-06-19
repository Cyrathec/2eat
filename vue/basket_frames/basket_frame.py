
from tkinter import *

from vue.base_frame import BaseFrame
from controller.basket_controller import BasketController


class BasketFrame(BaseFrame):
	
	def __init__(self, basket_controller: BasketController, master=None):
		super().__init__(master)
		self._basket_controller = basket_controller
		self._basket = self._basket_controller.getBasket(0) # possibilité d'avoir plusieur panier, pas de logique dans le programme donc on laisse toujours à 0
		self._create_widgets()

	def _create_widgets(self):

		self.title = Label(self, text="Basket:")
		self.title.grid(row=0, column=0)

		# grille
		yDefil = Scrollbar(self, orient='vertical')
		self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
		yDefil['command'] = self.listbox.yview
		self.listbox.bind('<<ListboxSelect>>', self.on_select)
		yDefil.grid(row=1, column=2, sticky='ns')
		self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

		self.price_entry = self.create_entry("Price: ", row=2)
		self.price_entry.config(state=DISABLED)
		self.restaurant_entry = self.create_entry("Restaurant: ", row=3)
		self.restaurant_entry.config(state=NORMAL)
		self.address_entry = self.create_entry("Shipment address: ", row=4)
		self.price_entry.config(state=NORMAL)
		# Return bouton
		self.menu = Button(self, text="Return", fg="red",
						   command=self.show_menu)
		self.menu.grid(row=5, column=0, sticky="w")
		self.clearb = Button(self, text="Clear", fg="red",
						   command=self.clear)
		self.update = Button(self, text="Update", fg="green",
						   command=self.update)
		self.order = Button(self, text="Order", fg="green",
						   command=self.order)

	def on_select(self, event):
		print("select")

	def show(self):
		self._basket = self._basket_controller.getBasket(0)
		self.listbox.delete(0, END)
		if len(self._basket) != 0:
			for index, product in enumerate(self._basket['products']):
				text = "{} ({}€)".format(product['name'].capitalize(), product['price'])
				self.listbox.insert(index, text)
			self.price_entry.config(state=NORMAL)
			self.price_entry.delete(0, END)
			self.price_entry.insert(0, str(self._basket['price'])+'€')
			self.price_entry.config(state=DISABLED)
			self.restaurant_entry.delete(0, END)
			self.restaurant_entry.insert(0, str(self._basket['restaurant']))
			self.address_entry.delete(0, END)
			self.address_entry.insert(0, str(self._basket['address']))
			self.clearb.grid(row=5, column=1, sticky="w")
			self.update.grid(row=5, column=2, sticky="w")
			self.order.grid(row=5, column=3, sticky="w")
		else:
			self.price_entry.config(state=NORMAL)
			self.price_entry.delete(0, END)
			self.price_entry.insert(0, "0.00€")
			self.price_entry.config(state=DISABLED)
			self.restaurant_entry.delete(0, END)
			self.address_entry.delete(0, END)
			self.clearb.grid_forget()
			self.update.grid_forget()
			self.order.grid_forget()
		super().show()

	def update(self):
		if str(self.restaurant_entry.get()) != str(self._basket['restaurant']):
			self._basket_controller.updateRestaurant(0, self.restaurant_entry.get())
		if str(self.address_entry.get()) != str(self._basket['address']):
			self._basket_controller.updateAddress(0, self.address_entry.get())
		self.show()

	def clear(self):
		self._basket_controller.delBasket(0)
		self.show()

	def order(self):
		self._root_frame.order_basket(self._basket)
		self.clear()
		messagebox.showinfo("Basket Ordered", "Your basket as been ordered, thanks for your purchase !")
