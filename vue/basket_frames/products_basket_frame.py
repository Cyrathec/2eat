
from tkinter import *

from vue.base_frame import BaseFrame
from controller.product_controller import ProductController


class ProductsBasketFrame(BaseFrame):
	
	def __init__(self, product_controller: ProductController, root_frame: Frame, restaurant=None):
		super().__init__(root_frame)
		self._product_controller = product_controller
		self._products = None
		self._restaurant = restaurant
		self._create_widgets()

	def _create_widgets(self):

		self.title = Label(self, text="List products:")
		self.title.grid(row=0, column=0)

		# grille
		yDefil = Scrollbar(self, orient='vertical')
		self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
		yDefil['command'] = self.listbox.yview
		self.listbox.bind('<<ListboxSelect>>', self.on_select)
		yDefil.grid(row=1, column=2, sticky='ns')
		self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

		# Return bouton
		self.add_to_basket_button = Button(self, text="Add to Basket", command=self.add_to_basket)
		self.menu = Button(self, text="Return", fg="red",
						   command=self.show_menu)
		self.menu.grid(row=4, column=0, sticky="w")

	def on_select(self, event):
		if len(self.listbox.curselection()) == 0:
			self.add_to_basket_button.grid_forget()
		else:
			self.add_to_basket_button.grid(row=3, sticky="nsew")

	def add_to_basket(self):
		if len(self.listbox.curselection()) == 0:
			self.add_to_basket_button.grid_forget()
		else:
			index = int(self.listbox.curselection()[0])
			product = self._products[index]
			self._root_frame.add_to_basket(product['id'], self._restaurant.get('id'))

	def show(self):
		if self._restaurant is None:
			self._products = self._product_controller.list_products()
		else:
			self._products = self._restaurant['products']
		self.listbox.delete(0, END)
		for index, product in enumerate(self._products):
			text = "{} ({}€)".format(product['name'].capitalize(), product['price'])
			self.listbox.insert(index, text)
		super().show()
