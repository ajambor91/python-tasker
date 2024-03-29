import tkinter
from tkinter import *
from classes.XML import XMLParser
from classes.CanvasArea import CanvasArea
class NoteListWindow(Tk):
    def __init__(self):
        super().__init__()
        self.__run__()


    def __parse_notes__(self):
        return self.xmlParser.parse_file()
    def __create_notes__(self):
        self.canvases = []
        print(self.notes)
        for note in self.notes:
            print('xxx')
            self.canvases.append(CanvasArea(self, note))
            # tkinter.Label(self.window, text=note).pack()
        self.mainloop()

    def __run__(self):
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", 'gray')
        self.wait_visibility()
        self.geometry("400x300-0-0")
        self.xmlParser = XMLParser()
        self.notes = self.__parse_notes__()
        self.__create_notes__()
