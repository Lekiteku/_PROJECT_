import random
import time
from geopy.distance import geodesic

class Location:
    @staticmethod
    def calculate_distance(live_location, student_list):
        for student in student_list:
            student_coords = (student['latitude'], student['longitude'])
            distance = geodesic(live_location, student_coords).meters
        return distance

    @staticmethod
    def assess_distances(live_location, student_list):
        set_limit = 500
        for distance in Location.calculate_distance(live_location, student_list):
            if distance < set_limit:
                print(f" It's {distance:.2f} kilometers away.")
            else:
                print(f"Distance from point A is {distance:.2f} kilometers.")

    @staticmethod
    def generate_random_coordinates():
            # Generate random latitude and longitude values
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
              # Wait for 1 second
        time.sleep(1)
            # Return the coordinates
        return latitude, longitude
    
        
      