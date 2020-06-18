from tkinter import *
from tkinter import messagebox

from vue.person_frames.person_formular_frame import PersonFormularFrame
from exceptions import Error

class PersonProfileFrame(PersonFormularFrame):

	def __init__(self, person_controller, person, master=None, editable=False, removable=False):
		self.editable = editable
		self.removable = removable
		super().__init__(master)
		self._person_controller = person_controller
		self._person = person
		self.refresh()

	def create_widgets(self):
		super().create_widgets()

		# Buttons
		if self.editable is True:
			self.edit_button = Button(self, text="Edit", command=self.edit)
			self.cancel_button = Button(self, text="Cancel", command=self.refresh)
			self.update_button = Button(self, text="Update", command=self.update)
		if self.removable is True:
			self.remove_button = Button(self, text="Remove", command=self.remove)
		self.return_button = Button(self, text="Return", fg="red", command=self.back)

		self.return_button.grid(row=20, column=0)
		if self.editable is True:
			self.edit_button.grid(row=20, column=1, sticky="nsew")
		if self.removable is True:
			self.remove_button.grid(row=20, column=2, sticky="nsew")

	def edit(self):
		self.edit_button.grid_forget()
		if self.removable is True:
			self.remove_button.grid_forget()
		entries = [self.firstname_entry, self.lastname_entry, self.password_entry, self.email_entry, self.address_entry]
		for entry in entries:
			entry.config(state=NORMAL)

		self.cancel_button.grid(row=20, column=2, sticky="nsew")
		self.update_button.grid(row=20, column=1, sticky="nsew")

	def _refresh_entry(self, entry, value=""):
		entry.delete(0, END)
		if value != "":
			entry.insert(0, value)
		entry.config(state=DISABLED)

	def refresh(self):
		# Restore window with person value and cancel edition
		if self.editable is True:
			self.cancel_button.grid_forget()
			self.update_button.grid_forget()
		self._refresh_entry(self.firstname_entry, self._person['firstname'])
		self._refresh_entry(self.lastname_entry, self._person['lastname'])
		self._refresh_entry(self.password_entry, self._person['password'])
		self._refresh_entry(self.email_entry, self._person['email'])
		self._refresh_entry(self.address_entry, self._person['address'])
		if self.editable is True:
			self.edit_button.grid(row=20, column=1, sticky="nsew")
		if self.removable is True:
			self.remove_button.grid(row=20, column=2, sticky="nsew")

	def update(self):
		data = self.get_data()
		person = self._person_controller.update_person(self._person['id'], data)
		self._person = person
		self.refresh()

	def remove(self):
		person_id = self._person['id']
		self._person_controller.delete_person(person_id)
		# show confirmation
		messagebox.showinfo("Success", "Person %s deleted !" % self._person['name'])
		self.back()