"""
CommunicationManager Class

This code defines the CommunicationManager class, a utility for managing parent information based on location indexes. It provides static methods for retrieving parent information, printing selected parents, and resetting used indexes.

Class Methods:
"""
import numpy as np

class CommunicationManager:
    """
    get_parent_info_by_location_index(parent_info, location_indexes, used_indexes):
    
    This static method takes three parameters:
    - parent_info: A NumPy array of parent information.
    - location_indexes: A NumPy array representing location indexes.
    - used_indexes: A set containing the indexes of previously used locations.
    
    It checks for available location indexes, finds the unused indexes, retrieves parent information for those indexes, and returns it.
    """
    @staticmethod
    def get_parent_info_by_location_index(parent_info, location_indexes, used_indexes):
        if location_indexes.size == 0:
            print("The 'location_indexes' array is empty.")
            return None

        # Find the unused indexes using NumPy set operations
        unused_indexes = np.setdiff1d(location_indexes, list(used_indexes))

        if unused_indexes.size == 0:
            print("All location indexes have been used.")
            return None

        # Get parent information corresponding to the unused indexes
        selected_parent_info = parent_info[unused_indexes]

        return selected_parent_info

    """0
    print_selected_parents(parent_info, selected_indexes):
    
    This static method takes two parameters:
    - parent_info: A NumPy array of parent information.
    - selected_indexes: A NumPy array containing the indexes of selected parents.
    
    It prints the names of selected parents corresponding to the given indexes.
    """
    @staticmethod
    def print_selected_parents(parent_info, selected_indexes):
        selected_parents = parent_info[selected_indexes]
        for parent in selected_parents:
            print("Selected Parent: ", parent)

    """
    reset_used_indexes(used_indexes):
    
    This static method takes a single parameter, used_indexes, which is a set that stores the used indexes. It clears the set of used indexes, effectively resetting it.
    """
    @staticmethod
    def reset_used_indexes(used_indexes):
        used_indexes.clear()

"""
The class is designed to be used without creating an instance. It separates the operations from the class instance, making it a useful utility for managing parent information without the need for class instantiation. The class itself doesn't have any instance attributes or methods that depend on the class state; all operations are performed based on the parameters provided to the static methods.
"""
