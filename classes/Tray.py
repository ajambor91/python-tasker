from pystray import MenuItem as item
from PIL import Image as ImageIcon

import pystray
from tkinter import *
import sys
import os
from classes.NoteWindow import NoteWindow
from classes.NoteListWindow import NoteListWindow

class Tray:
    def __init__(self):
        self._get_path()
        print(self.icon_path)
    def _get_path(self):
        self.icon_path = os.path.abspath(os.path.join(sys.path[0], 'resources\\tray_temp.ico'))
    def _action(self):
        print('sss')
        new_window = NoteWindow()
        pass
    def _create_notes_window(self):
        print('dddddddddddddddddddddddddddddddddd')
        self.note_list = NoteListWindow()
        pass
    def create_icon(self):
        image = ImageIcon.open(self.icon_path)
        menu = (item('name', self._create_notes_window, default=True), item('name', self._action))
        icon = pystray.Icon("name", image, "title", menu)


        try:
            icon.run()
        except Exception as e:
            print("Failed to register class:", e)
            return False
        return True


