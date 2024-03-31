from pystray import MenuItem as item
from PIL import Image as ImageIcon
from app.init import get_path
import pystray
from classes.NoteListWindow import NoteListWindow
from classes.NoteAddWindow import NoteAddWindow
from classes.AppMainWindow import AppMainWindow
class Tray:
    def __init__(self):
        self.icon_path = get_path('resources\\tray_temp.ico')
    def __add_note(self):
        new_window = NoteAddWindow()
        pass
    def __create_notes_window(self):
        self.note_list = NoteListWindow()
        pass
    def __show_main_window(self):
        self.note_list = AppMainWindow()
        pass
    def create_icon(self):
        image = ImageIcon.open(self.icon_path)
        menu = (
            item('Show notes',  self.__create_notes_window, default=True),
            item('Add note', self.__add_note),
            item('Show main window', self.__show_main_window))
        icon = pystray.Icon("name", image, "title", menu)
        try:
            icon.run()
        except Exception as e:
            return False
        return True


