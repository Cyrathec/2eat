from tkinter import *
from tkinter import messagebox

from vue.sport_frames.sport_formular_frame import SportFormularFrame
from exceptions import Error


class SportProfileFrame(SportFormularFrame):

    def __init__(self, sport_controller, sport, master=None):
        super().__init__(master)
        self._sport_controller = sport_controller
        self._sport = sport
        self.refresh()

    def create_widgets(self):
        super().create_widgets()

        # Buttons
        self.edit_button = Button(self, text="Edit",
                                  command=self.edit)
        self.cancel_button = Button(self, text="Cancel", command=self.refresh)
        self.update_button = Button(self, text="Update", command=self.update)
        self.remove_button = Button(self, text="Remove", command=self.remove)
        self.return_button = Button(self, text="Return", fg="red",
                                    command=self.back)

        self.return_button.grid(row=20, column=0)
        self.edit_button.grid(row=20, column=1, sticky="nsew")
        self.remove_button.grid(row=20, column=2, sticky="nsew")

    def edit(self):
        self.edit_button.grid_forget()
        self.remove_button.grid_forget()
        entries = [self.name_entry, self.description_entry]
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
        # Restore window with member value and cancel edition
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self._refresh_entry(self.name_entry, self._sport['name'])
        self.description_entry.delete("0.0", END)
        self.description_entry.insert("0.0", self._sport['description'])
        self.description_entry.config(state=DISABLED)
        self.edit_button.grid(row=20, column=1, sticky="nsew")
        self.remove_button.grid(row=20, column=2, sticky="nsew")

    def update(self):

        data = self.get_data()
        sport = self._sport_controller.update_sport(self._sport['id'], data)
        self._sport = sport
        self.refresh()

    def remove(self):
        sport_id = self._sport['id']
        self._sport_controller.delete_sport(sport_id)
        # show confirmation
        messagebox.showinfo("Success",
                            "Sport %s deleted !" % self._sport['name'])
        self.back()
