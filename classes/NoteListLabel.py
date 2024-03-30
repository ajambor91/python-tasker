from tkinter import Label


class NoteListLabel(Label):
    BACKGROUND_COLOR = '#f0e589'
    BORDER_WIDTH = 0
    FONT = ('Georgia', 14)

    def __init__(self, window, root, text):
        super().__init__(root,
                         text=text,
                         background=self.BACKGROUND_COLOR,
                         borderwidth=self.BORDER_WIDTH,
                         font=self.FONT)
        self.widow = window
        self.root = root
