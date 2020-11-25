"Main program file. This will use the methods.py file, and the Alarm.py file and will be the main run file for this program. This will also contain the GUI."
"Main program file. This will use the methods.py file, and the Alarm.py file and will be the main run file for this program. This will also contain the GUI."
from Alarm import *
from Methods import *


    # for Python3
from tkinter import *
from tkinter import messagebox

fileLoc = InitialiseStorageSystem()
global_Alarms = ReadAlarms(fileLoc)

def createAlarm(name, date, reminder, desc, contact, popup):
    Alarm(name, date, reminder,desc,contact).write_to_file(fileLoc)
    global_Alarms = ReadAlarms(fileLoc)
    popup.destroy()

def info_ButtonClick():
    popup = Tk()
    popup.wm_title("Enter Alarm Info")
    label = Label(popup, text="Alarm Name")
    label.pack(fill="both", pady=5, padx=5)
    name = Entry (popup)
    name.pack(fill="both", pady=5, padx=5)

    label1 = Label(popup, text="Alarm Time")
    label1.pack(fill="both", pady=5, padx=5)
    date = Entry (popup)
    date.pack(fill="both", pady=5, padx=5)

    label2 = Label(popup, text="Reminder")
    label2.pack(fill="both", pady=5, padx=5)
    reminder = Entry (popup)
    reminder.pack(fill="both", pady=5, padx=5)

    label3 = Label(popup, text="Description")
    label3.pack(fill="both", pady=5, padx=5)
    desc = Entry (popup)
    desc.pack(fill="both", pady=5, padx=5) 

    label4 = Label(popup, text="Contact (email)")
    label4.pack(fill="both", pady=5, padx=5)
    contact = Entry (popup)
    contact.pack(fill="both", pady=5, padx=5) 
    B1 = Button(popup, text="Continue", command = lambda:createAlarm(name.get(), date.get(), reminder.get(), desc.get(), contact.get(), popup))
    B1.pack(fill="both", pady=20, padx=20)
    popup.mainloop()

def ButtonClick():
    global_Alarms = ReadAlarms(fileLoc)
    output_str = ""
    for x in global_Alarms:
        output_str += x.__str__()
    if(len(output_str) > 0):
        messagebox.showinfo("Alarms",output_str)
    else:
        messagebox.showinfo("Alarms","No Alarms Created!")
    

form = Tk()
(form.winfo_toplevel()).title("SNEAKY SNEKS ALARM SYSTEM")

canvas1 = Canvas(form, width = 400, height = 400)

label1 = Label(form, text="Alarm System")
canvas1.create_window(200, 15, window= label1)

b = Button(form, text="View Alarms", command=lambda:ButtonClick())
canvas1.create_window(70, 75, window = b)

b1 = Button(form, text="Create New Alarm", command=lambda:info_ButtonClick())
canvas1.create_window(300, 75, window = b1)

canvas1.pack()

def SEND():
   # print("Checking time...")
    for x in global_Alarms:
        if(IsTime(x.get_alarm_date())):
            print("Sending email...")
            SendEmail(x)
            messagebox.showinfo("!!ALARM!!", x.__str__())

    form.after(3000, SEND)


form.after(3000, SEND)
form.mainloop()

