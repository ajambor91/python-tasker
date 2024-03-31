from tkinter import *
from app.utils import round_rectangle
from classes.NoteListLabel import NoteListLabel

class NoteListCanvas(Canvas):
     height = 300
     width = 400
     def __init__(self, window, text):
        super().__init__(window, highlightthickness=0)
        self.window = window
        self.label = NoteListLabel(window, self, text)
        self.__create_canvas()
        self.__add_label()
     def __create_canvas(self):
         self.create_rectangle(0, 0, 400, 400, fill='grey', outline='grey')
         self.canvas_area = self.__round_rectangle(0, 0, 400, 400, radius=20, fill="#f0e589")

         self.pack(fill='both')
     def __round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
         points = round_rectangle(x1, y1, x2, y2, radius=25, **kwargs)
         return self.create_polygon(points, **kwargs, smooth=True)
     def __add_label(self):
         self.create_window(200,100, anchor=CENTER , window=self.label, height=180, width=360)