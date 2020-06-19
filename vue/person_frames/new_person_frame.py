from tkinter import *
from tkinter import messagebox

from vue.person_frames.person_formular_frame import PersonFormularFrame
from exceptions import Error

class NewPersonFrame(PersonFormularFrame):

    def __init__(self, person_controller, master=None):
        super().__init__(master)
        self._person_controller = person_controller

    def create_widgets(self):
        super().create_widgets()
        self.valid = Button(self, text="valid", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="cancel", fg="red",
                             command=self.back)
        self.valid.grid(row=20, column=1, sticky=E)
        self.cancel.grid(row=20, column=2, sticky=W)
    
    def valid(self):
        data = self.get_data()
        try:
            member_data = self._person_controller.create_person(data)
            messagebox.showinfo("Success",
                                "Person %s %s created !" % (member_data['firstname'], member_data['lastname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu(member_data)