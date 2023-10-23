import random
import time
import numpy as np

class Location:
    @staticmethod
    def haversine_distance(coord1, coord2):
        # Radius of the Earth in meters
        earth_radius = 6371000

        lat1, lon1 = np.radians(coord1)
        lat2, lon2 = np.radians(coord2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

        distance = earth_radius * c
        return distance

    @staticmethod
    def calculate_distance(live_location, student_list):
        distances = []
        for student in student_list:
            student_coords = (student['latitude'], student['longitude'])
            distance = Location.haversine_distance(live_location, student_coords)
            distances.append(distance)
        return np.array(distances)

    @staticmethod
    def assess_distances(live_location, student_list):
        set_limit = 500
        distances = Location.calculate_distance(live_location, student_list)
        for distance in distances:
            if distance < set_limit:
                print(f"It's {distance:.2f} meters away.")
            else:
                print(f"Distance from point A is {distance:.2f} meters.")

    @staticmethod
    def generate_random_coordinates(num_coordinates):
        # Generate random latitude and longitude values used to simulate GPS coordinates
        latitudes = np.random.uniform(-90, 90, size=num_coordinates)
        longitudes = np.random.uniform(-180, 180, size=num_coordinates)

        # Wait for 1 second
        time.sleep(1)

        # Return the coordinates as a NumPy array
        return np.column_stack((latitudes, longitudes))

    @staticmethod
    def generate_random_live_location():
        # Generate a single random live location
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        # Wait for 1 second
        time.sleep(1)

        # Return the live location as a tuple
        return latitude, longitude

# Example usage:
num_coordinates = 32  # Specify the number of coordinates you want to generate
student_list = [{'latitude': 52.5200, 'longitude': 13.4050}, {'latitude': 48.8566, 'longitude': 2.3522}]
live_location = Location.generate_random_live_location()

Location.assess_distances(live_location, student_list)
random_coordinates = Location.generate_random_coordinates(num_coordinates)
print(f"Random Live Location: {live_location}")
print("Random Coordinates:")
print(random_coordinates)
