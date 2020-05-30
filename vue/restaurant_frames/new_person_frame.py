from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class NewPersonFrame(BaseFrame):

    def __init__(self, person_controller, master=None):
        super().__init__(master)
        self._person_controller = person_controller
        self.create_widgets()
        self.name_pattern = re.compile("^[a-zA-Z-]{2,50}$")
        self.email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

    def create_widgets(self):

        Label(self, text="Data informations:", font='bold').grid(row=0, sticky='w')
        self.firstname_entry = self.create_entry("Firstname", row=1, validate_callback=self.validate_name)
        self.lastname_entry = self.create_entry("Lastname", row=2, validate_callback=self.validate_name)
        self.email_entry = self.create_entry("Email", row=3, validate_callback=self.validate_email)
        self.medical_certificate = BooleanVar()
        self.medical_certificate.set(False)

        Label(self, text="Address:", font='bold').grid(row=10, sticky='w')
        self.street_entry = self.create_entry("Street", row=11)
        self.postal_code_entry = self.create_entry("Postal Code", row=12, validate_callback=self.validate_postal_code)
        self.city_entry = self.create_entry("City", row=13)
        self.country_entry = self.create_entry("Country", row=14)

        self.valid = Button(self, text="valid", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="cancel", fg="red",
                             command=self.back)
        self.valid.grid(row=20, column=1, sticky=E)
        self.cancel.grid(row=20, column=2, sticky=W)

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
        data = dict(firstname=self.firstname_entry.get(),
                    lastname=self.lastname_entry.get(),
                    email=self.email_entry.get())

        if self.street_entry.get() != "" and self.city_entry.get() != "" and \
                re.match("[\d]+", self.postal_code_entry.get()):
            address = dict(street=self.street_entry.get(),
                           postal_code=int(self.postal_code_entry.get()),
                           city=self.city_entry.get())
            if self.country_entry.get() != "":
                address['country'] = self.country_entry.get()
            data['address'] = address
        return data

    def valid(self):
        data = self.get_data()
        try:
            member_data = self._person_controller.create_person(data)
            messagebox.showinfo("Success",
                                "Member %s %s created !" % (member_data['firstname'], member_data['lastname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.back()
