from tkinter import *
from tkinter import messagebox

from vue.sport_frames.sport_formular_frame import SportFormularFrame
from exceptions import Error


class NewSportFrame(SportFormularFrame):

    def __init__(self, sport_controller, master=None):
        super().__init__(master)
        self._sport_controller = sport_controller

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
            sport_data = self._sport_controller.create_sport(data)
            messagebox.showinfo("Success",
                                "Sport %s created !" % sport_data['name'])

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.back()
