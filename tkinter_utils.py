from tkinter import *


class EntryLabelFrame(Frame):

    def __init__(self, master, label_text):
        super().__init__(master)
        Label(self, text=label_text).grid(row=0, column=0)

        self.string_var = StringVar()
        Entry(self, textvariable=self.string_var).grid(row=0, column=1, sticky="WE")

    def get(self):
        return self.string_var.get()
