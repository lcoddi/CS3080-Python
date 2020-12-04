"""
Methods file
This file contains methods for use in the main program
"""
import os
from datetime import datetime # for getting current time
import ezgmail  # for sending email, may need to pip install ezgmail
from Alarm import *

# This method will set up the file system. If the file exists
# then it will return the path; if the file doesn’t exist it
# will create the file and return the log path. 
def InitialiseStorageSystem():
    fileName = 'Sneaky_Sneks_Alarm_Program_File.txt'
    path = os.getcwd()
    fullLogPath = path+'\\'+fileName
    try:
        file = open(fullLogPath, "a")
    except:
        print("Creating file...")

    return fullLogPath
        
        
# This method will get the file and read in information from
# the flat file containing the other alarms and create an
# array of Alam class objects.
# The Alarm class WriteValue() function returns  a string of the class variables comma delimited as follows:
# Name,Date,ReminderTime,Description,email
#
# The file to be read from should look something like this,
# depending on how the Alarms() method is written:
# Wake Up,10-24-2020/08:00,time to do homework,rlong2@uccs.edu
# Store,10-25-2020/13:00,halloween shopping,foo@bar.com

def ReadAlarms(path_to_file):
    
    #global alarms
    alarms = []
    with open(path_to_file, "r") as filestream:
        for line in filestream:
            if(len(line) > 1):
                currentLine = line.split(",")
                name = currentLine[0]
                date = currentLine[1]
                reminder = currentLine[2]
                description = currentLine[3]
                contact = currentLine[4]
                alarms.append(Alarm(name, date, reminder, description, contact))

           # print(alarms[name])
    return alarms

#This method will send the email to the given contact for the alarm.
#the contact will be a part of an alarm class.
# The token.json and credentials.json authenticate access to cs3080python@gmail.com,
# so any sent email comes from that address.
# Syntax: ezgmail.send(recipient_email, "Subject Line", "Email body")
def SendEmail(alarm):

    # create variables for sending through ezgmail
    email_address = alarm.get_alarm_contact()
    name = alarm.get_alarm_name()
    description = alarm.get_alarm_description()
    reminder = alarm.get_alarm_reminder()

    # email body
    body = '''
 This is your scheduled reminder that the following task is due %s

 Alarm Title: %s
 Alarm Description: %s
  ''' % (reminder, name, description)
    
    # Send the email
    ezgmail.send(email_address, name, body)
    
    return 0

#check if the alarm time has come up
# Returns true if the time for the alarm has arrived and false if not.
# Return null if it is in the past. This will need to be run in the background
def IsTime(alarmTime):
    currentTime = datetime.now()
    currentTime = currentTime.strftime("%m-%d-%Y/%H:%M")
    if (currentTime == alarmTime):
        return True
    else:
        return False

