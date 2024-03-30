from tkinter import Tk
from classes.NoteListCanvas import NoteListCanvas
from services.NotesService import NotesService
class NoteListWindow(Tk):
    def __init__(self):
        self.notes_service = NotesService()
        super().__init__()
        self.__run()
        self.notes = self.__parse_notes()
        self.__create_notes()
    def __parse_notes(self):
        return self.notes_service.parse_file()
    def __create_notes(self):
        self.canvases = []
        print(self.notes)
        for note in self.notes:
            print('xxx')
            self.canvases.append(NoteListCanvas(self, note))
            # tkinter.Label(self.window, text=note).pack()
        self.mainloop()

    def __run(self):
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", 'gray')
        self.wait_visibility()
        self.geometry("400x300-0-0")

