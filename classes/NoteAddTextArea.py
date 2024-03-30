from tkinter import Text


class NoteAddTextArea(Text):
    BACKGROUND_COLOR = '#f0e589'
    BORDER_WIDTH = 0
    FONT = ('Georgia', 14)

    def __init__(self, window, root):
        super().__init__(root,
                         background=self.BACKGROUND_COLOR,
                         borderwidth=self.BORDER_WIDTH,
                         font=self.FONT)
        self.widow = window
        self.root = root
