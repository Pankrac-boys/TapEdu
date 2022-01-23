#Build with Pygubu. Used .ui file in res directory
import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
import cvis
import numpy as np
from PIL import ImageGrab

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "interface.ui"

class App:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = tk.Frame(self.root)
        self.frame2.configure(background='#ffffff', height='50', width='2000')
        self.frame2.pack(side='top')
        self.frame1 = tk.Frame(self.root)
        self.frame5 = tk.Frame(self.frame1)
        self.button3 = tk.Button(self.frame5)
        self.button3.configure(activebackground='#ffffff', background='#ffffff', compound='left', cursor='arrow')
        self.button3.configure(font='{@Arial} 12 {}', foreground='#6f81ff', relief='flat', text='Predict')
        self.button3.pack(side='left')
        self.button3.configure(command=self.predict)
        self.button9 = tk.Button(self.frame5)
        self.button9.configure(activebackground='#ffffff', background='#ffffff', compound='left', cursor='arrow')
        self.button9.configure(font='{@Arial} 12 {}', foreground='#6f81ff', relief='flat', text='Export')
        self.button9.pack(side='left')
        self.button9.configure(command=self.export)
        self.frame5.configure(height='200', width='2000')
        self.frame5.pack(side='top')
        self.frame1.configure(background='#ffffff', height='200', width='2000')
        self.frame1.pack(anchor='nw', side='top')
        self.calculator = tk.Frame(self.root)
        self.labelCalculator = tk.Label(self.calculator)
        self.labelCalculator.configure(background='#ffffff', cursor='arrow', font='{@Ariel} 12 {}', foreground='#6f81ff')
        self.labelCalculator.configure(relief='flat', text='Calculator')
        self.labelCalculator.pack(anchor='nw', padx='20', pady='10', side='top')
        self.frame4 = tk.Frame(self.calculator)
        self.frame4.configure(background='#ffffff', height='700', width='400')
        self.frame4.pack(side='top')
        self.calculator.configure(background='#ffffff', height='800', width='400')
        self.calculator.pack(anchor='w', side='left')
        self.cv = tk.Canvas(self.root)
        self.cv.configure(background='#ffffff', cursor='pencil', height='800', relief='flat')
        self.cv.configure(width='800')
        self.cv.pack(anchor='center', pady='100', side='top')
        self.cv.bind('<B1-Motion>', self.draw, add='')
        self.cv.bind('<Button-1>', self.get_x_and_y, add='')
        self.root.configure(cursor='arrow', height='1000', width='1000')
        self.root.geometry('1920x1080')
        self.root.title('TabEdu')

        # Main widget
        self.mainwindow = self.root
    
    def run(self):
        self.mainwindow.mainloop()

    def predict(self):
        x=self.root.winfo_rootx()+self.cv.winfo_x()
        y = self.root.winfo_rooty()+self.cv.winfo_y()
        x1=x+self.cv.winfo_width()
        y1=y+self.cv.winfo_height()
        img = ImageGrab.grab().crop((x,y,x1,y1))
        img = np.array(img)
        img = img[:, :, ::-1].copy()  
        cvis.run(img)

    def export(self):
        x=self.root.winfo_rootx()+self.cv.winfo_x()
        y = self.root.winfo_rooty()+self.cv.winfo_y()
        x1=x+self.cv.winfo_width()
        y1=y+self.cv.winfo_height()
        img = ImageGrab.grab().crop((x,y,x1,y1))
        img.save("ex.jpg")

    def draw(self, event):
        global lasx, lasy
        self.cv.create_line((lasx, lasy, event.x, event.y), fill='black', width=5)
        lasx, lasy = event.x, event.y

    def get_x_and_y(self, event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

if __name__ == '__main__':
    app = App()
    app.run()


