from tkinter import *
from classes.NoteAddCanvas import NoteAddCanvas
from services.NotesService import NotesService
class NoteAddWindow(Tk):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 250
    X_CORD = 10
    Y_CORD = 60
    def __init__(self):
        super().__init__()
        self.notes_service = NotesService()
        self.note_add_canvas = NoteAddCanvas(self)

        self.__run()
    def on_save_action(self):
        self.__save_note()
    def __get_note_content(self):
        text = self.note_add_canvas.text_area.get("1.0", "end-1c")
        return text
    def __save_note(self):
        self.notes_service.parse_data(data=self.__get_note_content())
    def __run(self):
        self.overrideredirect(True)
        self.lift()
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", 'gray')
        self.wait_visibility()
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}-{self.X_CORD}-{self.Y_CORD}")
        self.mainloop()
