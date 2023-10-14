import os
class Person:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.registered = False

        # Create a folder for the person based on their name
        self.create_folder()

    def register(self):
        self.registered = True

    def create_folder(self):
        base_folder = "photos"
        folder_name = os.path.join(base_folder, f"{self.first_name}_{self.last_name}")
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder for {self.first_name} {self.last_name} in the 'photos' folder.")

class Parent(Person):
    def __init__(self, first_name, last_name, gender, guardian_name, phone_number):
        super().__init__(first_name, last_name, gender)
        self.guardian_name = guardian_name
        self.phone_number = phone_number

class Checkpoint:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class Student(Person):
    def __init__(self, first_name, last_name, gender, student_id, checkpoint, parents=None):
        super().__init__(first_name, last_name, gender)
        self.student_id = student_id
        self.checkpoint = checkpoint
        self.parents = parents if parents is not None else []

    def register(self):
        self.registered = True


class UnknownIndividual:
    def __init__(self, face_encoding, timestamp, location, additional_info=None):
        self.face_encoding = face_encoding  # Facial encoding data
        self.timestamp = timestamp  # Date and time of the encounter
        self.location = location  # Location of the encounter
        self.additional_info = additional_info  # Additional information about the encounter (optional)

    def __str__(self):
        return f"Timestamp: {self.timestamp}, Location: {self.location}, Additional Info: {self.additional_info}"

class SchoolBusStaff(Person):
    def __init__(self, first_name, last_name, gender, staff_id, role):
        super().__init__(first_name, last_name, gender)
        self.staff_id = staff_id
        self.role = role

    def register(self):
        self.registered = True

        # Example usage:
if __name__ == "__main__":
    person1 = Student("John", "Doe", "Male", 44545 , )

    # Check if folders were created
    if os.path.exists("John_Doe"):
        print("Folder for John Doe exists.")
   

