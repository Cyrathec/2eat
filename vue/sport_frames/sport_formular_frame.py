from tkinter import *

from vue.base_frame import BaseFrame


class SportFormularFrame(BaseFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.name_pattern = re.compile("^[a-zA-Z-]{2,50}$")

    def create_widgets(self):

        Label(self, text="Data informations:", font='bold').grid(row=0, sticky='w')
        self.name_entry = self.create_entry("Name: ", row=1, validate_callback=self.validate_name)
        Label(self, text="Descripton: ").grid(row=2, sticky="w")
        self.description_entry = Text(self, fg='black')
        self.description_entry.grid(row=3, column=0, columnspan=3)

    def validate_name(self, event, entry=None):
        if not self.name_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def get_data(self):
        data = dict(name=self.name_entry.get(),
                    description=self.description_entry.get("0.0", "end"))
        return data
