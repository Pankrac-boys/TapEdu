import tkinter as tk
import canvas, panel
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('TapEdu')
        self.configure(bg = "lightgrey")
        width  = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f'{width}x{height}')
        self.state("zoomed")

if __name__ == "__main__":
    app = App()
    upperPanel = panel.Panel(app)
    def get_x_and_y(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def draw(event):
        global lasx, lasy
        cv.create_line((lasx, lasy, event.x, event.y), fill='black', width=5)
        lasx, lasy = event.x, event.y
    
    cv = tk.Canvas(app)
    cv.bind("<Button-1>", get_x_and_y)
    cv.bind("<B1-Motion>", draw)
    cv.configure(bg = "white")
    cv.pack()  
    app.mainloop()
