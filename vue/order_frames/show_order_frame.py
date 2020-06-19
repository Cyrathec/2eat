
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from vue.base_frame import BaseFrame
from functools import partial

class ShowOrderFrame(BaseFrame):

	def __init__(self, order_controller, order, master=None, isAdmin=False):
		super().__init__(master)
		self._order_controller = order_controller
		self._order = order
		self._isAdmin = isAdmin
		self._create_widgets()

	def _create_widgets(self):

		self.title = Label(self, text="Order N°" + str(self._order['id']))
		self.title.grid(row=0, column=0)

		# grille
		yDefil = Scrollbar(self, orient='vertical')
		self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
		yDefil['command'] = self.listbox.yview
		self.listbox.bind('<<ListboxSelect>>')
		yDefil.grid(row=1, column=2, sticky='ns')
		self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

		self.price_entry = self.create_entry("Price: ", row=2)
		self.price_entry.config(state=DISABLED)
		self.address_entry = self.create_entry("Shipment address: ", row=4)
		self.price_entry.config(state=DISABLED)
		# Return bouton
		self.menu = Button(self, text="Return", fg="red",
						   command=self.show_menu)
		self.menu.grid(row=5, column=0, sticky="w")
		if self._isAdmin:
			self.delete = Button(self, text="Delete the order", fg="red",
							   command=self.delete)
			self.delete.grid(row=5, column=1, sticky="w")


	def show(self):
		self.listbox.delete(0, END)
		if len(self._order) != 0:
			for index, product in enumerate(self._order['products']):
				text = "{} ({}€)".format(product['name'].capitalize(), product['price'])
				self.listbox.insert(index, text)
			self.price_entry.config(state=NORMAL)
			self.price_entry.delete(0, END)
			self.price_entry.insert(0, str(round(self._order['price'],2))+'€')
			self.price_entry.config(state=DISABLED)
			self.address_entry.config(state=NORMAL)
			self.address_entry.delete(0, END)
			self.address_entry.insert(0, str(self._order['address']))
			self.address_entry.config(state=DISABLED)
		super().show()

	def delete(self):
		self._order_controller.deleteOrder(self._order['id'])
		self.show_menu()