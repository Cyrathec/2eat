from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
	def __init__(self, root_frame, person=None, asAdmin=False):
		super().__init__(root_frame)
		self._as_admin = asAdmin
		self.person = person
		self.create_widgets()

	def create_widgets(self):
		self.title = Label(self, text="Welcome in 2eat App, {}".format(self.person["firstname"]))

		"""
		Menu displays differently when the person is a user or an admin :
			- User can order from a restaurant and can see his pending orders
			- Admin can manage all restaurants, products, orders and users. He also have the option to use the app as a regular user
		"""

		if self._as_admin == True:
			self.restaurants = Button(self, text="Restaurants", width=30, command=self._root_frame.show_restaurants)
			self.products = Button(self, text="Products", width=30, command=self._root_frame.show_products)
			self.users = Button(self, text="Users", width=30, command=self._root_frame.show_persons)
		
		self.profile = Button(self, text="Profile", width=30, command=self.show_person_profile)

		self.quit = Button(self, text="QUIT", fg="red", width=30, command=self.quit)

		self.title.pack(side="top")

		if self._as_admin == True:
			self.restaurants.pack()
			self.products.pack()
			self.users.pack()
		
		self.profile.pack()

		self.quit.pack(side="bottom")

	def show_person_profile(self):
		self._root_frame.show_person(self.person["id"], editable=True)
