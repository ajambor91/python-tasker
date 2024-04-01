from tkinter import ttk


class NoteAddTextArea(ttk.Label):
    BACKGROUND_COLOR = '#f0e589'
    BORDER_WIDTH = 0
    FONT = ('Georgia', 14)

    def __init__(self, root):
        super().__init__(root,
                         text='TEST')
        self.root = root
