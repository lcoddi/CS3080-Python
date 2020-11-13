"Create Alarm Class here for the CS3080 python final project."

# This is a PLACEHOLDER Alarm class to test initial functionality of the ReadAlarms() method
# This class still needs to write to a file

class Alarm:
    def __init__(self, name="default_name", time="12:00", description="default_description", email="default@email.com"):
                 self.name = name
                 self.time = time
                 self.description = description
                 self.email = email
    def __str__(self):
        return "Name: " + self.name + "\nTime due: " + self.time + "\nDescription: " + self.description + "\nEmail: " + self.email

