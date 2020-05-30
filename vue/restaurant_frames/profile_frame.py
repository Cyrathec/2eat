
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from vue.base_frame import BaseFrame
from functools import partial


class ProfileFrame(BaseFrame):

    def __init__(self, person_controller, sport_controller, person, master=None):
        super().__init__(master)
        self._person = person
        print(self._person)
        self._person_controller = person_controller
        self._sport_controller = sport_controller
        self._sports = []
        self._name_pattern = re.compile("^[\S-]{2,50}$")
        self._email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="%s profile: " % self._person.get('type', '').capitalize(), font='bold')
        self.title.grid(row=0, column=0, sticky=W)

        self.firstname_entry = self.create_entry("Firstname: ", row=1, validate_callback=self.validate_name,
                                                 columnspan=3)
        self.lastname_entry = self.create_entry("Lastname: ", row=2, validate_callback=self.validate_name,
                                                columnspan=3)
        self.email_entry = self.create_entry("Email: ", row=3, validate_callback=self.validate_email,
                                             columnspan=4)
        if self._person['type'] == 'person':
            self.medical_certificate = BooleanVar()
            self.medical_certificate.set(self._person['medical_certificate'])
            self.medical_certificate_ckeck = Checkbutton(self, text="Medical certificate",
                                                         variable=self.medical_certificate)
            self.medical_certificate_ckeck.grid(row=4)
        elif self._person['type'] == 'coach':
            self.contract_entry = self.create_entry("contract: ", row=4, columnspan=4)
            self.degree_entry = self.create_entry("degree: ", row=5, columnspan=4)

        Label(self, text="Address:", font='bold').grid(row=10, sticky='w')
        self.street_entry = self.create_entry("Street: ", row=11, columnspan=4)
        self.postal_code_entry = self.create_entry("Postal Code: ", row=12, validate_callback=self.validate_postal_code,
                                                   columnspan=2)
        self.city_entry = self.create_entry("City: ", row=13, columnspan=3)
        self.country_entry = self.create_entry("Country: ", row=14, columnspan=3)

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

        # Sport Frame
        self.sports_frame = Frame(self)
        self.sports_frame.grid(row=0, column=6, rowspan=20, sticky="n", padx=10)
        self.list_sports_frame = None

    def validate_name(self, event, entry=None):
        if not self._name_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def validate_email(self, event, entry=None):
        if not self._email_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def validate_postal_code(self, event, entry=None):
        if not re.match("[\d]+", entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def edit(self):
        self.edit_button.grid_forget()
        self.remove_button.grid_forget()
        entries = [self.firstname_entry, self.lastname_entry, self.email_entry, self.street_entry,
                   self.postal_code_entry, self.city_entry, self.country_entry]
        if self._person['type'] == 'coach':
            entries += [self.contract_entry, self.degree_entry]
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
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self._refresh_entry(self.firstname_entry, self._person['firstname'])
        self._refresh_entry(self.lastname_entry, self._person['lastname'])
        self._refresh_entry(self.email_entry, self._person['email'])
        address = self._person.get('address', {})
        self._refresh_entry(self.street_entry, address.get('street', ''))
        self._refresh_entry(self.postal_code_entry, str(address.get('postal_code', '')))
        self._refresh_entry(self.city_entry, address.get('city', ''))
        self._refresh_entry(self.country_entry, address.get('country', ''))
        if self._person['type'] == 'person':
            self.medical_certificate.set(self._person['medical_certificate'])
        elif self._person['type'] == 'coach':
            self._refresh_entry(self.degree_entry, self._person['degree'])
            self._refresh_entry(self.contract_entry, self._person['contract'])
        self.edit_button.grid(row=20, column=1, sticky="nsew")
        self.remove_button.grid(row=20, column=2, sticky="nsew")
        self.refresh_sports()

    def refresh_sports(self):

        if self.list_sports_frame is not None:
            self.list_sports_frame.destroy()
        self.list_sports_frame = Frame(master=self.sports_frame)
        self.list_sports_frame.grid(row=1, columnspan=3, sticky="w")

        Label(self.list_sports_frame, text="Sports: ", font='bold').grid(row=0, sticky="w")
        i = 1
        if "sports" in self._person:
            for sport in self._person['sports']:
                self.list_sports_frame.columnconfigure(i, weight=1)
                Label(self.list_sports_frame, text=sport['name']).grid(row=i, column=0, sticky="w")
                Label(self.list_sports_frame, text=sport['level']).grid(row=i, column=1, sticky="w")
                del_button = Button(self.list_sports_frame, text="-", command=partial(self.delete_sport, sport['id']))
                del_button.grid(row=i, column=2, sticky="w")
                i += 1

        # Add sport
        self.choose_sport_box = ttk.Combobox(self.list_sports_frame, values=[sport['name'] for sport in self._sports])
        self.level_box = ttk.Combobox(self.list_sports_frame, values=["beginner", "high", "professional"])
        self.add_sport_button = Button(self.list_sports_frame, text="+", command=self.add_sport)

        self.choose_sport_box.grid(row=i, column=0, stick="nsew")
        self.level_box.grid(row=i, column=1, stick="nsew")
        self.add_sport_button.grid(row=i, column=2, stick="w")

    def update(self):

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

        if self._person['type'] == 'person':
            data['medical_certificate'] = bool(self.medical_certificate.get())
            person = self._person_controller.update_person(self._person['id'], data)
        elif self._person['type'] == 'coach':
            data['contract'] = self.contract_entry.get()
            data['degree'] = self.degree_entry.get()
            person = self._person_controller.update_coach(self._person['id'], data)
        else:
            person = self._person_controller.update_person(self._person['id'], data)
        self._person = person
        self.refresh()

    def remove(self):
        person_id = self._person['id']
        self._person_controller.delete_person(person_id)
        # show confirmation
        messagebox.showinfo("Success",
                            "person %s %s deleted !" % (self._person['firstname'], self._person['lastname']))
        self.back()

    def get_sport_id(self, name):
        for sport in self._sports:
            if sport['name'] == name:
                return sport['id']
        return None

    def add_sport(self):
        sport_name = self.choose_sport_box.get()
        level = self.level_box.get()
        if sport_name != "" and level != "":
            sport_id = self.get_sport_id(sport_name)
            if sport_id is not None:
                self._person = self._person_controller.add_sport_person(self._person['id'], sport_id, level)
            else:
                messagebox.showerror("Sport %s not found" % sport_name)
        self.refresh_sports()

    def delete_sport(self, sport_id):

        self._person = self._person_controller.delete_sport_person(self._person['id'], sport_id)
        self.refresh_sports()

    def show(self):
        self._sports = self._sport_controller.list_sports()
        self.refresh()
        super().show()
