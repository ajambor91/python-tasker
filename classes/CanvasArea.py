from tkinter import *
from classes.XML import XMLParser
class CanvasArea(Canvas):
     # background_color = '#fff'
     height = 300
     width = 400

     def __init__(self, window, text):
        super().__init__(window, highlightthickness=0)
        self.window = window
        self.create_rectangle(0,0,400,400, fill='grey', outline='grey')
        self.canvas_area = self.round_rectangle(0, 0, 400, 400, radius=20, fill="#f0e589")

        self.pack(fill='both')
        print('text', text)
        pass

     def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
         points = [x1 + radius, y1,
                   x1 + radius, y1,
                   x2 - radius, y1,
                   x2 - radius, y1,
                   x2, y1,
                   x2, y1 + radius,
                   x2, y1 + radius,
                   x2, y2 - radius,
                   x2, y2 - radius,
                   x2, y2,
                   x2 - radius, y2,
                   x2 - radius, y2,
                   x1 + radius, y2,
                   x1 + radius, y2,
                   x1, y2,
                   x1, y2 - radius,
                   x1, y2 - radius,
                   x1, y1 + radius,
                   x1, y1 + radius,
                   x1, y1]

         return self.create_polygon(points, **kwargs, smooth=True)
     # def get_notes(self):
     #     self.xmlParser = XMLParser()
     #     list = self.xmlParser.parse_file()
     #     for note in list:
     #         print('x', note)
     #         tkinter.Label(self.window, text=note).pack()