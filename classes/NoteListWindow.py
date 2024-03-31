from tkinter import Tk
from classes.NoteListCanvas import NoteListCanvas
from services.NotesService import NotesService

class NoteListWindow(Tk):
    def __init__(self):
        super().__init__()
        self.notes_service = NotesService()
        self.__run()
        self.notes = self.__parse_notes()
        self.__create_notes()
    def __parse_notes(self):
        return self.notes_service.parse_file()
    def __create_notes(self):
        self.canvases = []
        print(self.notes)
        for note in self.notes:
            self.canvases.append(NoteListCanvas(self, note))
        self.mainloop()

    def __run(self):
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", 'gray')
        self.wait_visibility()
        self.geometry("400x300-0-0")

