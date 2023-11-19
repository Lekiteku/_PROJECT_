import random
import time
import numpy as np
import math

class LocationManager:
  
    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
        """
        Calculate the Haversine distance between a single set of latitude and longitude and an array of coordinates.
        The result is in meters.
        """
    # Radius of the Earth in meters
        earth_radius = 6371000  # 6371 km converted to meters

    # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = np.radians(lat2)
        lon2 = np.radians(lon2)

    # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

        # Calculate the distance in meters
        distance = earth_radius * c
        return distance
   
    @staticmethod
    def assess_distance(lat1, lon1, lat2_array, lon2_array, distance_threshold):
        # Calculate the Haversine distance using the existing haversine_distance function
        distances = LocationManager.haversine_distance(lat1, lon1, lat2_array, lon2_array)

        # Check if the distances are greater than the specified threshold
        indices = np.where(distances > distance_threshold)[0]

        return indices

    @staticmethod
    def generate_random_coordinates(num_coordinates):
        # Generate random latitude and longitude values used to simulate GPS coordinates
        latitudes = np.random.uniform(-90, 90, size=num_coordinates)
        longitudes = np.random.uniform(-180, 180, size=num_coordinates)

        # Wait for 1 second
        time.sleep(1)

        # Return the coordinates as a NumPy array
        return latitudes, longitudes

    @staticmethod
    def generate_random_live_location():
        # Generate a single random live location
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        # Wait for 1 second
        time.sleep(1)

        # Return the live location as a tuple
        return latitude, longitude
