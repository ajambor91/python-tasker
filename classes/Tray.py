from pystray import MenuItem as item
from PIL import Image as ImageIcon
from app.init import get_path
import pystray
import sys
import os
from classes.NoteWindow import NoteWindow
from classes.NoteListWindow import NoteListWindow

class Tray:
    def __init__(self):
        self.icon_path = get_path('resources\\tray_temp.ico')

    def _get_path(self):
        self.icon_path = os.path.abspath(os.path.join(sys.path[0], 'resources\\tray_temp.ico'))
    def _action(self):
        new_window = NoteWindow()
        pass
    def _create_notes_window(self):
        self.note_list = NoteListWindow()
        pass
    def create_icon(self):
        image = ImageIcon.open(self.icon_path)
        menu = (item('Show notes', self._create_notes_window, default=True), item('Add note', self._action))
        icon = pystray.Icon("name", image, "title", menu)
        try:
            icon.run()
        except Exception as e:
            return False
        return True


