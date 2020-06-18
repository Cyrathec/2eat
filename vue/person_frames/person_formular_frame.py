from tkinter import *

from vue.base_frame import BaseFrame

class PersonFormularFrame(BaseFrame):

	def __init__(self, master=None):
		super().__init__(master)
		self.create_widgets()
		self.name_pattern = re.compile("^[a-zA-Z-]{2,50}$")
		self.email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

	def create_widgets(self):

		Label(self, text="Data informations:", font='bold').grid(row=0, sticky='w')
		self.firstname_entry = self.create_entry("Firstname", row=1, validate_callback=self.validate_name)
		self.lastname_entry = self.create_entry("Lastname", row=2, validate_callback=self.validate_name)
		self.email_entry = self.create_entry("Email", row=3, validate_callback=self.validate_email)
		self.password_entry = self.create_entry("Password", row=4)
		
		self.address_entry = self.create_entry("Address", row=5)

		"""
		Label(self, text="Address:", font='bold').grid(row=10, sticky='w')
		self.street_entry = self.create_entry("Street", row=11)
		self.postal_code_entry = self.create_entry("Postal Code", row=12, validate_callback=self.validate_postal_code)
		self.city_entry = self.create_entry("City", row=13)
		self.country_entry = self.create_entry("Country", row=14)
		"""

	def validate_name(self, event, entry=None):
		if not self.name_pattern.match(entry.get()):
			entry.config(fg='red')
		else:
			entry.config(fg='black')

	def validate_postal_code(self, event, entry=None):
		if not re.match("[\d]+", entry.get()):
			entry.config(fg='red')
		else:
			entry.config(fg='black')

	def validate_email(self, event, entry=None):
		if not self.email_pattern.match(entry.get()):
			entry.config(fg='red')
		else:
			entry.config(fg='black')

	def get_data(self):
		#str(hash(self.password_entry.get()))
		
		address = self.address_entry.get()
		"""
		if self.street_entry.get() != "" and self.city_entry.get() != "":
			address += self.street_entry.get()
			address += " "
			address += self.city_entry.get()
			address += " "
			address += self.postal_code_entry.get()
			address += " "
			if self.country_entry.get() != "":
				address += self.country_entry.get()
		"""

		data = dict(firstname=self.firstname_entry.get(),
					lastname=self.lastname_entry.get(),
					email=self.email_entry.get(), password = self.password_entry.get(), isAdmin=False, address=address)

		# a user signed up from within the software is never an admin, thus isAdmin=False

		return data
