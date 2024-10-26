import tkinter as tk

window = tk.Tk()

window.geometry("500x500")
window.title("My 100th Python GUI")

label = tk.Label(window, text="PYTHON GUI", font=('Arial', 18))
label.pack(padx=20, pady=20)


textbox = tk.Text(window, height=3, font=('Arial', 16))  


myentry = tk.Entry(window)  

button = tk.Button(window, text="Click Me!", font=('Arial', 16)) 
button.pack(padx=10, pady=10)

window.mainloop()
