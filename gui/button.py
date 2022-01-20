import tkinter as tk
from PIL import ImageGrab
class Button(tk.Button):
    def __init__(self, win, text):
        self = tk.Button(win, text = text, bg = "lightblue")
        self.pack()

    #TODO Funkce na export nakreslene tabule do obrazku
    def export():
        x=root.winfo_rootx()+widget.winfo_x()
        y = root.winfo_rooty()+widget.winfo_y()
        x1=x+widget.winfo_width()
        y1=y+widget.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save("image.jpg")
