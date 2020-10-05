"Main program file. This will use the methods.py file, and the Alarm.py file and will be the main run file for this program. This will also contain the GUI."
"Main program file. This will use the methods.py file, and the Alarm.py file and will be the main run file for this program. This will also contain the GUI."
from Alarm import *
from Methods import *


    # for Python3
from tkinter import *
from tkinter import messagebox


def info_ButtonClick():
    popup = Tk()
    popup.wm_title("Enter Alarm Info")
    label = Label(popup, text="Alarm Name")
    label.pack(fill="both", pady=20, padx=20)
    entry1 = Entry (popup)
    entry1.pack(fill="both", pady=20, padx=20)
    label1 = Label(popup, text="Alarm Time")
    label1.pack(fill="both", pady=20, padx=20)
    entry2 = Entry (popup)
    entry2.pack(fill="both", pady=20, padx=20) 
    B1 = Button(popup, text="Continue", command = lambda:(messagebox.showinfo("Value from box", entry1.get())))
    B1.pack(fill="both", pady=20, padx=20)
    popup.mainloop()

def ButtonClick():
    messagebox.showinfo("Already Created Alarms","This will show all previous alarm info")
    

form = Tk()
(form.winfo_toplevel()).title("SNEAKY SNEKS ALARM SYSTEM")

canvas1 = Canvas(form, width = 400, height = 400)

label1 = Label(form, text="Alarm System")
canvas1.create_window(200, 15, window= label1)

b = Button(form, text="View Old Alarms", command=lambda:ButtonClick())
canvas1.create_window(70, 75, window = b)

b1 = Button(form, text="Create New Alarm", command=lambda:info_ButtonClick())
canvas1.create_window(300, 75, window = b1)

canvas1.pack()

mainloop()

