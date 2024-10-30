"""Hello World Application for Tkinter"""

from tkinter import * #not recommended (using * )
from tkinter.ttk import *

root = Tk()
label = Label(root, text="Hello World")
label2 = Label(root, text ="Y0000000")
button1 = Button(root, text="CLICK MEE!!!")
button2 = Button(root, text="Don't CLICK!")
label.pack()
label2.pack()
button1.pack()
button2.pack()
root.mainloop()

############
