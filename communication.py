#communication control will run here gsm
        
import numpy as np


class CommunicationManager:
    # A static method to enable location communication
    @staticmethod
    def enable_location_communication():
        print(10)
    # A static method to disable location communication
    @staticmethod
    def location_communication():
        print(12)
        
# A static method to enable location communication
    @staticmethod
    def enable_location_communication():
        print(3)



# Sample list of names
names = np.array(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack"])

# Sample list of indexes as a NumPy array
indexes = np.array([])

if indexes.size == 0:
    print("The 'indexes' array is empty.")
else:
    # Find the names corresponding to the indexes
    selected_names = names[indexes]
    
    # Print the selected names
    for name in selected_names:
        print(name)
