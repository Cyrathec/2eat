
from tkinter import *

from vue.base_frame import BaseFrame
from controller.person_controller import PersonController

class ListPersonsFrame(BaseFrame):

	def __init__(self, person_controller: PersonController, root_frame: Frame, display_admins_only=None):
		super().__init__(root_frame)
		self._person_controller = person_controller

		self._members = None

		# can be [True, False, None]. If is None, displays users and admins
		self._display_admins_only = display_admins_only

		self._create_widgets()

	def _create_widgets(self):

		self.title = Label(self, text="List Users:")
		self.title.grid(row=0, column=0)

		# grille
		yDefil = Scrollbar(self, orient='vertical')
		self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
		yDefil['command'] = self.listbox.yview
		self.listbox.bind('<<ListboxSelect>>', self.on_select)
		yDefil.grid(row=1, column=2, sticky='ns')
		self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

		self.show_person_button = Button(self, text="Show profile", command=self.show_person)

		# Return bouton
		self.menu = Button(self, text="Return", fg="red", command=self.show_menu)
		self.menu.grid(row=4, column=0, sticky="w")

	def on_select(self, event):
		if len(self.listbox.curselection()) == 0:
			self.show_person_button.grid_forget()
		else:
			self.show_person_button.grid(row=3, column=1, sticky="nsew")

	def show_person(self):
		if len(self.listbox.curselection()) == 0:
			self.show_person_button.grid_forget()
		else:
			index = int(self.listbox.curselection()[0])
			person = self._members[index]
			self._root_frame.show_person(person['id'])

	def show(self):
		self._members = self._person_controller.list_persons(self._display_admins_only)
		self.listbox.delete(0, END)
		for index, person in enumerate(self._members):
			text = "{} {}".format(person['firstname'], person['lastname'])
			self.listbox.insert(index, text)
		super().show()