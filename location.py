import random
import time
from geopy.distance import geodesic


student_data = [
    {
        "latitude": 52.5200,
        "longitude": 13.4050,
        "email": "student1@example.com",
        "name": "John Doe",
        "parent_phone": "123-456-7890"
    },
    {
        "latitude": 48.8566,
        "longitude": 2.3522,
        "email": "student2@example.com",
        "name": "Jane Smith",
        "parent_phone": "987-654-3210"
    },
    {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "email": "student3@example.com",
        "name": "Bob Johnson",
        "parent_phone": "555-123-4567"
    }
]

class Location:
    @staticmethod
    def calculate_distance(point_a, points_b):
        for name, coords in points_b:
            distance = geodesic(point_a, coords).kilometers
        return distance

    @staticmethod
    def assess_distances(point_a, points_b):
        results = []
        for name, distance in Location.calculate_distance(point_a, points_b):
            if distance < 500:
                results.append(f"You are almost there to {name}! It's {distance:.2f} kilometers away.")
            else:
                results.append(f"Distance from point A to {name} is {distance:.2f} kilometers.")
        return results

    @staticmethod
    def generate_random_coordinates():
            # Generate random latitude and longitude values
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
              # Wait for 1 second
        time.sleep(1)
            # Return the coordinates
        return latitude, longitude
        
      


# Point A coordinates (e.g., a fixed location)
point_a = (40.7128, -74.0060)  # New York City coordinates


# Get a generator for random coordinates


# Calculate the distance between Point A and a random location # Get the first random location
while True:
    random_coordinate_generator = Location.generate_random_coordinates()
    lat , long = random_coordinate_generator
    print(f"{lat} latitude and {long}")
    