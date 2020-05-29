from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Welcome in BDS App")
        #self.subscribe = Button(self, text="Subscribe", width=30, command=self._root_frame.show_subscribe)
        #self.new_coach = Button(self, text="New coach", width=30, command=self._root_frame.new_coach)
        #self.new_sport = Button(self, text="New sport", width=30, command=self._root_frame.new_sport)
        self.members = Button(self, text="Members", width=30, command=self._root_frame.show_members)
        self.coaches = Button(self, text="Coaches", width=30, command=self._root_frame.show_coaches)
        self.sports = Button(self, text="Sports", width=30, command=self._root_frame.show_sports)
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
        #self.subscribe.pack()
        #self.new_coach.pack()
        #self.new_sport.pack()
        self.members.pack()
        self.coaches.pack()
        self.sports.pack()
        self.quit.pack(side="bottom")
