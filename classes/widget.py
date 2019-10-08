import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from .logic import *

class Application(tk.Frame, logic):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.createWidgets()

    def takeTime(self, hour, minute, nOrD):
        if self.alarm(hour, minute, nOrD):
            while True:
                self.startMusic()
                messagebox.showinfo("Alarm", "Time!")
                time.sleep(3)
                break

    def createWidgets(self):
        self.wBgImage = ImageTk.PhotoImage((Image.open('.\\source\\img\\bg.jpg')))
        self.bgLable = tk.Label(self)
        self.bgLable['image'] = self.wBgImage
        self.bgLable.place(x=0, y=0, relwidth=1, relheight=1)

        self.wCommbox1 = ttk.Combobox(self)
        self.wCommbox1['values'] = self.housReturn()
        self.wCommbox1['height'] = '8'
        self.wCommbox1.set(time.strftime("%I"))
        self.wCommbox1.grid(row=0, column=0, columnspan=4)

        self.wCommbox2 = ttk.Combobox(self)
        self.wCommbox2['values'] = self.minuteReturn()
        self.wCommbox2['height'] = '8'
        self.wCommbox2.set(time.strftime("%M"))
        self.wCommbox2.grid(row=0, column=4, columnspan=4)

        self.wCommbox3 = ttk.Combobox(self)
        self.wCommbox3['values'] = ['PM', 'AM']
        self.wCommbox3['height'] = '3'
        self.wCommbox3.set(time.strftime("%p"))
        self.wCommbox3.grid(row=0, column=8, columnspan=4)

        self.wLable = tk.Label(self)
        self.wLable['text'] = "{}: {}".format('Current time', time.strftime("%I:%M %p"))
        self.wLable.grid(row=1, column=0, columnspan=14)

        self.wButton = tk.Button(self)
        self.wButton["text"] = "Setup"
        self.wButton["command"] = lambda:self.takeTime(self.wCommbox1.get(), self.wCommbox2.get(), self.wCommbox3.get())
        self.wButton.grid(row=0, column=13, columnspan=3)

    def housReturn(self):
        self.hous = []
        for x in range(1, 13): self.hous.append(str(x))
        return self.hous

    def minuteReturn(self):
        self.minute = []
        for x in range(1, 61): self.minute.append(str(x))
        return self.minute