import tkinter
from tkinter import *
from classes.XML import XMLParser
class NoteListWindow:
    def __init__(self):
        self.window = Tk()
        self.window.configure(bg='#fff')
        self.window.overrideredirect(True)
        # add widgets here

        # self.window.title('Hello Python')
        self.window.geometry("400x200-10-20")
        self.parse_notes()
        self.window.mainloop()
        self.window.wait_visibility()
    def parse_notes(self):
        self.xmlParser = XMLParser()
        list = self.xmlParser.parse_file()
        for note in list:
            print('x',note)
            tkinter.Label(self.window, text=note).pack()
