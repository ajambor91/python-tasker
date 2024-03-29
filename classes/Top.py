from tkinter import *
from classes.Tray import Tray
from classes.NoteListWindow import NoteListWindow
from classes.NoteWindow import NoteWindow
class Top():
    def __init__(self):
        self.app_tray = Tray()

    def run_app(self):
        self.app_tray.create_icon()
