"""
Alarm Class

Private fields:
Name - gives the alarm name
Date - used for when the alarm is created format: (mm-dd-yyyy/hh:mm). Default is to use the current time + 1hr.
reminderTime - another date used for when to send the email. Default is equal to the date; format:  (mm-dd-yyyy/hh:mm)
Description - basic alarm description given by user
Contact- email to send to when alarm ‘goes off’

Public Fields:
Getters and setters for all the above variables
Constructor to initialize all the above private fields
WriteValue() - returns  a string of the class variables comma delimited as follows: Name,Date,ReminderTime,Description,email
SendToFile(FileLoc) - Writes the WriteValue() method’s value to the storage file (FileLoc).
"""

import re

class Alarm:

#constructor
    def __init__(self, alarm_name="default_name", alarm_date="12:00", alarm_reminder="13:00", alarm_description="default_description", alarm_contact="default_contact"):
        self.alarm_name = alarm_name
        self.alarm_date = alarm_date
        self.alarm_reminder = alarm_reminder
        self.alarm_description = alarm_description
        self.alarm_contact = alarm_contact

 # return the string form of the class
    def __str__(self):
        return "Name: " + self.alarm_name + "\nDate: " + self.alarm_date + "\nReminder Time: " + self.alarm_reminder + "\nDescription: " + self.alarm_description + "\nEmail: " + self.alarm_contact

# Getters
    def get_alarm_name(self):
        return self.alarm_name

    def get_alarm_date(self):
        return self.alarm_date

    def get_alarm_reminder(self):
        return self.alarm_reminder

    def get_alarm_description(self):
        return self.alarm_description

    def get_alarm_contact(self):
        return self.alarm_contact

# Setters
    def set_alarm_name(self, name):
        self.alarm_name = name

    def set_alarm_date(self, date):
        self.alarm_date = date

    def set_alarm_reminder(self, reminder):
        self.alarm_reminder = reminder

    def set_alarm_description(self, description):
        self.alarm_description = description

    def set_alarm_contact(self, contact):
        self.alarm_contact = contact

#write the class to a file
    def write_to_file(self, FileLoc):
        f = open(FileLoc, "a")
        f.write(self.alarm_name + "," + self.alarm_date + "," + self.alarm_reminder + "," + self.alarm_description + "," + self.alarm_contact + "\n")
        f.close()    

'''
Example of how to use:

a1 = Alarm()

a1.set_alarm_name(input('enter Alarm name: '))

a1.set_alarm_date('11-15-2020/0 8:00')
a1.set_alarm_description('time to do homework')
a1.set_alarm_contact('rlong2@uccs.edu')

a1.write_to_file(a1.get_alarm_name(), a1.get_alarm_date(), 'now', a1.get_alarm_description(), a1.get_alarm_contact())
print(a1.get_alarm_date())
'''
