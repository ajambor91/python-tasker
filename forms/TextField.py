from tkinter import Entry


class TextField(Entry):
    BACKGROUND_COLOR = '#f0e589'
    BORDER_WIDTH = 0
    FONT = ('Georgia', 14)

    def __init__(self, root, value):
        super().__init__(root, textvariable=value)
        self.root = root
        self.pack()

