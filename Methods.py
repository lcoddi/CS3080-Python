"Add methods for the CS3080 Python final Project here."
import os

# This method will set up the file system. If the file exists
# then it will return the path; if the file doesn’t exist it
# will create the file and return the log path. 
def InitialiseStorageSystem():
    fileName = '\Sneaky_Sneks_Alarm_Program_File.txt'
    path = os.getcwd()
    fullLogPath = path+'\\'+filename
    try:
        file = open(fullLogPath, "a")
    except:
        print("Creating file...")

    return fullLogPath
        
        
# This method will get the file and read in information from
# the flat file containing the other alarms and create an
# array of Alam class objects. (Call the INITialiseStorageSystem() methoed to get
# the path of the log file.)
def ReadAlarms():
    return 0

#This method will send the email to the given contact for the alarm.
#the contact will be apart of an alarm class.
def Ring():
    return 0


# Returns true if the time for the alarm has arrived and false if not.
# Return null if it is in the past. This will need to be run in the background
def IsTime():
    return 0

