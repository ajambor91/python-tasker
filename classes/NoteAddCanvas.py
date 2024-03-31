from tkinter import *
from app.utils import round_rectangle
from classes.NoteAddTextArea import NoteAddTextArea
from classes.NoteAddButton import NoteAddButton

class NoteAddCanvas(Canvas):
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 250
    X_CORD = 10
    Y_CORD = 30

    def __init__(self, window):
        super().__init__(window, highlightthickness=0, height=self.WINDOW_HEIGHT, width=self.WINDOW_WIDTH)
        self.window = window
        self.text_area = NoteAddTextArea(window, self)
        self.btn = NoteAddButton(window, self)
        self.__create_canvas()
        self.__add_text_area()

    def __create_canvas(self):
        self.create_rectangle(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, fill='grey', outline='grey')
        self.canvas_area = self.__round_rectangle(0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, radius=20, fill="#f0e589")
        self.__add_save_button()
        self.pack(fill='both')

    def __round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = round_rectangle(x1, y1, x2, y2, radius=25, **kwargs)
        return self.create_polygon(points, **kwargs, smooth=True)

    def __add_save_button(self):
        self.create_window(20, 240, anchor=SW, window=self.btn)

    def __add_text_area(self):
        self.create_window(200,100, anchor=CENTER , window=self.text_area, height=180, width=360)
        pass
    def _get_note_content(self):
        text = self.text_area.get("1.0", "end-1c")
        return text
