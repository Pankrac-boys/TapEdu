import tkinter as tk
#FIXME nez se vyresi bs s argumentama, pouzivat imperativni pristup
class Canvas(tk.Canvas):
    def get_x_and_y(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def draw(widget, event):
        global lasx, lasy
        widget.create_line((lasx, lasy, event.x, event.y), fill='black', width=5)
        lasx, lasy = event.x, event.y
    
    def __init__(self, win):
        self = tk.Canvas(win, width = 500, height = 500, bg = "white")
        
        #FIXME args shit
        self.bind("<Button-1>", lambda : self.get_x_and_y())
        self.bind("<B1-Motion>", lambda : self.draw(self))
        
        self.pack(anchor = "center");
