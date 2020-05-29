from tkinter import *
from tkinter import messagebox

from vue.member_frames.new_person_frame import NewPersonFrame
from exceptions import Error


class NewCoachFrame(NewPersonFrame):

    def __init__(self, person_controller, master=None):
        super().__init__(person_controller, master)

    def create_widgets(self):
        super().create_widgets()
        self.contract_entry = self.create_entry("contract: ", row=4, columnspan=4)
        self.degree_entry = self.create_entry("degree: ", row=5, columnspan=4)

    def valid(self):

        data = super().get_data()
        data['contract'] = self.contract_entry.get()
        data['degree'] = self.degree_entry.get()

        try:
            member_data = self._person_controller.create_coach(data)
            messagebox.showinfo("Success",
                                "Member %s %s created !" % (member_data['firstname'], member_data['lastname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
