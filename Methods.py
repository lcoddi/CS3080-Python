"Add methods for the CS3080 Python final Project here."
import os
import datetime # for getting current time

# This method will set up the file system. If the file exists
# then it will return the path; if the file doesn’t exist it
# will create the file and return the log path. 
def InitialiseStorageSystem():
    fileName = '\Sneaky_Sneks_Alarm_Program_File.txt'
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
    
    global alarms
    alarms = {}
    with open(path + "\\" + fileName, "r") as filestream:
        for line in filestream:
            currentLine = line.split(",")
            name = currentLine[0]
            time = currentLine[1]
            description = currentLine[2]
            email = currentLine[3]
            alarms[name] = Alarm(name, time, description, email)

            print(alarms[name])

#This method will send the email to the given contact for the alarm.
#the contact will be apart of an alarm class.
def SendEmail(alarm1):
    return 0


# Returns true if the time for the alarm has arrived and false if not.
# Return null if it is in the past. This will need to be run in the background
def IsTime(alarmTime):
    currentTime = datetime.datetime.now()
    # May need to convert time to format (mm-dd-YYYY/hh:mm) like so:
    # currentTime = currentTime.strftime("%m-%d-%Y/%H:%M")
    if (currentTime >= alarmTime):
        return True
    else:
        return False

