from tkinter import *

from vue.base_frame import BaseFrame


class ProductFormularFrame(BaseFrame):

	def __init__(self, master=None):
		super().__init__(master)
		self.create_widgets()
		self.name_pattern = re.compile("^[a-zA-Z- ]{2,50}$")
		self.price_pattern = re.compile("^\d+(?:\.\d{0,2})?$")

	def create_widgets(self):

		Label(self, text="Data informations:", font='bold').grid(row=0, sticky='w')
		self.name_entry = self.create_entry("Name: ", row=1, validate_callback=self.validate_name)
		self.price_entry = self.create_entry("Price: ", row=2, validate_callback=self.validate_price)

	def validate_name(self, event, entry=None):
		if not self.name_pattern.match(entry.get()):
			entry.config(fg='red')
		else:
			entry.config(fg='black')

	def validate_price(self, event, entry=None):
		if not self.price_pattern.match(entry.get()):
			entry.config(fg='red')
		else:
			entry.config(fg='black')

	def get_data(self):
		data = dict(name=self.name_entry.get(), price=float(self.price_entry.get()))
		return data
