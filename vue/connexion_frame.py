from tkinter import Frame, Label, Entry
from tkinter import *
from tkinter import messagebox

import logging


from functools import partial
from vue.base_frame import BaseFrame
from exceptions import Error



class ConnexionFrame(BaseFrame):
    def __init__(self, person_controller, master=None):
        super().__init__(master)
        self._person_controller = person_controller
        self._email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        self._create_widgets()

    def show(self):
        self.grid(padx=10, pady=10)

    def hide(self):
        self.grid_forget()

    def quit(self):
        self._root_frame.quit()

    def _create_widgets(self):

        self.title = Label(self, text="connexion")
        self.title.grid(row=0, column=0, sticky=W)

       
        self.email_entry = self.create_entry("Email: ", row=0, validate_callback=self.validate_email)
        self.password_entry = self.create_entry("Password: ", row=1)
       
        # Buttons
        self.connexion_button = Button(self, text="Connexion", fg="Blue",
                                  command=self.connexion)
        self.cancel_button = Button(self, text="Erase", fg="Blue", command=self.refresh)
        self.inscription_button = Button(self, text="Inscription", fg="Blue", command=self.inscription)
        
        self.inscription_button.grid(row=20, column=2)
        self.connexion_button.grid(row=20, column=0, sticky=E)
        self.cancel_button.grid(row=20, column=1, sticky=W)

    def inscription(self):
        self._root_frame.new_member()
     
    def refresh(self):
        self._refresh_entry(self.password_entry, '')
        self._refresh_entry(self.email_entry, '')
        
    def _refresh_entry(self, entry, value=""):
        entry.delete(0, END)
        if value != "":
            entry.insert(0, value)
        
    def validate_email(self, event, entry=None):
        if not self._email_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def show_menu(self,member_data=None):
        self._root_frame.show_menu(member_data)

    def connexion(self):
        try:
            member_data = self._person_controller.connexion(self.email_entry.get(), self.password_entry.get())
            if member_data != {0}:
                messagebox.showinfo("Connexion success !" )
                self._root_frame.show_menu(member_data)
            else:
                messagebox.showinfo("Try again")
                self.refresh()
        except Error as e:
            logging.info("Error Menu")
            messagebox.showerror("Error", str(e))
            return

    def show(self):
        self.refresh()
        self.grid(padx=100, pady=100)
