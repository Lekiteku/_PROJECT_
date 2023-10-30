from location import LocationManager
from database import DatabaseManager
from communication import CommunicationManager

DatabaseManager.set_database_file("manijo.db")
DatabaseManager.create_database()
students_info, parents_infor ,lat ,long = DatabaseManager.get_data_arrays()

while True:
    lat ,long = LocationManager.generate_random_live_location
    lat_array ,long_array = LocationManager.generate_random_coordinates(200)
    indixes = LocationManager.assess_distance(lat,long,lat_array,long_array, 500)
    CommunicationManager.get_parent_info_by_location_index()

