from tkinter import *

from vue.menu_frame import MenuFrame
from vue.member_frames.new_member_frame import NewMemberFrame
from vue.member_frames.list_members_frame import ListMembersFrame
from vue.member_frames.profile_frame import ProfileFrame


class RootFrame(Frame):
    """
    Member actions
    help: http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html
    """

    def __init__(self, person_controller, master=None):
        super().__init__(master)
        self._person_controller = person_controller
        self._menu_frame = MenuFrame(self)
        self._frames = []

    def new_member(self):
        self.hide_frames()
        # Show formular subscribe
        subscribe_frame = NewMemberFrame(self._person_controller, self)
        subscribe_frame.show()
        self._frames.append(subscribe_frame)


    def show_members(self):

        # show members
        self.hide_menu()
        list_frame = ListMembersFrame(self._person_controller, self, person_type='member')
        self._frames.append(list_frame)
        list_frame.show()
        
   

    def show_profile(self, member_id):
        member_data = self._person_controller.get_person(member_id)

        self.hide_frames()
        profile_frame = ProfileFrame(self._person_controller, member_data, self)
        self._frames.append(profile_frame)
        profile_frame.show()

 

  

    def hide_frames(self):
        for frame in self._frames:
            frame.hide()

    def show_menu(self):
        for frame in self._frames:
            frame.destroy()
        self._frames = []
        self._menu_frame.show()

    def hide_menu(self):
        self._menu_frame.hide()

    def back(self):
        if len(self._frames) <= 1:
            self.show_menu()
            return
        last_frame = self._frames[-1]
        last_frame.destroy()
        del(self._frames[-1])
        last_frame = self._frames[-1]
        last_frame.show()

    def cancel(self):
        self.show_menu()

    def quit(self):
        self.master.destroy()
