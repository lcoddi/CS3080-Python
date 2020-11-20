import re
"Create Alarm Class here for the CS3080 python final project."
"""
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


class Alarm:

    def __init__(self, alarm_name="", alarm_date="", alarm_reminder="", alarm_description="", alarm_contact=""):
        self.__alarm_name = alarm_name
        self.__alarm_date = alarm_date
        self.__alarm_reminder = alarm_reminder
        self.__alarm_description = alarm_description
        self.__alarm_contact = alarm_contact
# Getters

    def get_alarm_name(self):
        return self.__alarm_name

    def get_alarm_date(self):
        return self.__alarm_date

    def get_alarm_reminder(self):
        return self.__alarm_reminder

    def get_alarm_description(self):
        return self.__alarm_description

    def get_alarm_contact(self):
        return self.__alarm_contact
# Setters

    def set_alarm_name(self, name):
        self.__alarm_name = name

    def set_alarm_date(self, date):
        self.__alarm_date = date

    def set_alarm_reminder(self, reminder):
        self.__alarm_reminder = reminder

    def set_alarm_description(self, description):
        self.__alarm_description = description

    def set_alarm_contact(self, contact):
        self.__alarm_contact = contact

    def write_to_file(self, name, date, reminder, description, contact):
        f = open("text.txt", "a")
        f.write(name + "," + date + "," + reminder + "," + description + "," + contact + "\n")
        f.close()


a1 = Alarm()
"""
a1.set_alarm_name(input('enter name'))

a1.set_alarm_date('11-15-2020/08:00')
a1.set_alarm_description('time to do homework')
a1.set_alarm_contact('rlong2@uccs.edu')

a1.write_to_file(a1.get_alarm_name(), a1.get_alarm_date(), 'now', a1.get_alarm_description(), a1.get_alarm_contact())
print(a1.get_alarm_date())
"""
