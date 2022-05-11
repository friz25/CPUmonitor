import tkinter as tk
from trinter import ttk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 0.5) #прозрачность от 0 до 1
        self.attributes('-topmost', True) #поверх всех окон
        self.overrideredirect(True) #убираем рамку окна
        self.resizable(False, False)
        self.title('CPU-RAM usage monitor bar')

        self.set_ui()

    def set_ui(self):
        ttk.Button(self, text='Exit').pack()


root = Application()
root.mainloop()