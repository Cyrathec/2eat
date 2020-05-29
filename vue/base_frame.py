from tkinter import Frame, Label, Entry, DISABLED
from functools import partial


class BaseFrame(Frame):
    def __init__(self, root_frame):
        super().__init__(root_frame.master, width=300)
        self._root_frame = root_frame

    def show(self):
        self.grid(padx=10, pady=10)

    def hide(self):
        self.grid_forget()

    def quit(self):
        self._root_frame.quit()

    def back(self):
        self._root_frame.back()

    def create_entry(self, label, row=0, width=50, validate_callback=None, text=None,
                     disabled=False, columnspan=3, **options):
        Label(self, text=label).grid(row=row, sticky="w")
        entry = Entry(self, width=width, fg='black', **options)
        if text:
            entry.insert(0, text)
        if disabled:
            entry.config(state=DISABLED)
        if validate_callback:
            entry.bind('<KeyRelease>', partial(validate_callback, entry=entry))
        entry.grid(row=row, column=1, columnspan=columnspan)
        return entry

    def show_menu(self):
        self._root_frame.show_menu()
