"A better Hello World for tkinter"

import tkinter as tk
from tkinter import ttk

class HelloView(tk.Frame):
    """A freindly little module"""
    def __init__(self, parent, *args, **kwargs):
        super(). __init__(parent, *args, **kwargs)

self.name = tk.StringVar()
self.hello_string = tk.StringVar()
self.hello_string.set("Hello World")

name_label = ttk.Label(self, text="Name:")
name_entry = ttk.Entry(self, textvariable=self.name)

ch_button =ttk.Button(self, text="Change", command=self.on_charge)

hello_label = ttk.Label(self, textvariable = self.hello_string,
    font=("TkDefaultFont", 64), wraplength=600)
