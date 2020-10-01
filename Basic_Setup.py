    # for Python3
from tkinter import *
from tkinter import messagebox


def info_ButtonClick():
    popup = Tk()
    popup.wm_title("Test pop up")
    label = Label(popup, text="You clicked the more info button")
    label.pack(fill="both", pady=20, padx=20)
    entry1 = Entry (popup)
    entry1.pack(fill="both", pady=20, padx=20) 
    B1 = Button(popup, text="Continue", command = lambda:(messagebox.showinfo("Value from box", entry1.get())))
    B1.pack(fill="both", pady=20, padx=20)
    popup.mainloop()

def ButtonClick(boxText):
    messagebox.showinfo("Information display", "Text is: " + boxText)
    

form = Tk()
(form.winfo_toplevel()).title("GUI Example")

canvas1 = Canvas(form, width = 400, height = 400)

entry1 = Entry (form) 
canvas1.create_window(75, 75, window=entry1)

label1 = Label(form, text="Hello world")
canvas1.create_window(200, 15, window= label1)

b = Button(form, text="Click Me", command=lambda:ButtonClick(entry1.get()))
canvas1.create_window(30, 150, window = b)

b1 = Button(form, text="Enter More Info", command=lambda:info_ButtonClick())
canvas1.create_window(50, 200, window = b1)

canvas1.pack()

mainloop()

