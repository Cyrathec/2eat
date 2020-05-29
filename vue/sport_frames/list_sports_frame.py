
from tkinter import *

from vue.base_frame import BaseFrame
from controller.sport_controller import SportController


class ListSportsFrame(BaseFrame):

    def __init__(self, sport_controller: SportController, root_frame: Frame):
        super().__init__(root_frame)
        self._sport_controller = sport_controller

        self._sports = None
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="List sports:")
        self.title.grid(row=0, column=0)

        # grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        yDefil.grid(row=1, column=2, sticky='ns')
        self.listbox.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # Return bouton
        self.new_sport_button = Button(self, text="New Sport", command=self._root_frame.new_sport)
        self.show_sport_button = Button(self, text="Show profile", command=self.show_sport)
        self.menu = Button(self, text="Return", fg="red",
                           command=self.show_menu)
        self.new_sport_button.grid(row=3, sticky="nsew")
        self.menu.grid(row=4, column=0, sticky="w")

    def on_select(self, event):
        if len(self.listbox.curselection()) == 0:
            self.show_sport_button.grid_forget()
        else:
            self.show_sport_button.grid(row=3, column=1, sticky="nsew")

    def show_sport(self):
        if len(self.listbox.curselection()) == 0:
            self.show_sport_button.grid_forget()
        else:
            index = int(self.listbox.curselection()[0])
            sport = self._sports[index]
            self._root_frame.show_sport(sport['id'])

    def show(self):
        self._sports = self._sport_controller.list_sports()
        self.listbox.delete(0, END)
        for index, sport in enumerate(self._sports):
            text = sport['name'].capitalize()
            self.listbox.insert(index, text)
        super().show()
