
from tkinter import *

from vue.base_frame import BaseFrame
from controller.order_controller import OrderController


class ListOrderFrame(BaseFrame):
	
	def __init__(self, order_controller : OrderController, client_id: str, master=None):
		super().__init__(master)
		self._order_controller = order_controller
		self._client_id = client_id
		self._orders = self._order_controller.searchOrdersByClient(self._client_id)
		self._create_widgets()

	def _create_widgets(self):

		self.title = Label(self, text="Orders:")
		self.title.grid(row=0, column=0)

		# grille
		yDefil = Scrollbar(self, orient='vertical')
		self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
		yDefil['command'] = self.listbox.yview
		self.listbox.bind('<<ListboxSelect>>', self.on_select)
		yDefil.grid(row=1, column=2, sticky='ns')
		self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

		# Return bouton
		self.show_order_button = Button(self, text="Show order", command=self.show_order)
		self.menu = Button(self, text="Return", fg="red",
						   command=self.show_menu)
		self.menu.grid(row=2, column=0, sticky="w")

	def on_select(self, event):
		if len(self.listbox.curselection()) == 0:
			self.show_order_button.grid_forget()
		else:
			self.show_order_button.grid(row=2, column=1, sticky="w")

	def show(self):
		self._orders = self._order_controller.searchOrdersByClient(self._client_id)
		self.listbox.delete(0, END)
		if len(self._orders) != 0:
			for index, order in enumerate(self._orders):
				text = "N°{} ({}€)".format(order['id'], order['price'])
				self.listbox.insert(index, text)		
		super().show()

	def show_order(self):
		if len(self.listbox.curselection()) == 0:
			self.show_order_button.grid_forget()
		else:
			index = int(self.listbox.curselection()[0])
			order = self._orders[index]
			self._root_frame.show_order(order)