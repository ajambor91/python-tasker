from tkinter import *
 class CanvasArea(Canvas):
     background_color = ''
     height = 100
     width = 200
     def __init__(self):
         super().__init__(background=self.background_color)

