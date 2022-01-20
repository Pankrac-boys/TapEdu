import tkinter as tk
import button
class Panel(tk.PanedWindow):
    def __init__(self, win):
        self = tk.PanedWindow(win, orient = tk.VERTICAL, bg = "blue")
        export = button.Button(self, "Export")
        predict = button.Button(self, "Predict")
        self.pack()
