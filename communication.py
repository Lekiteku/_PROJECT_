import socket
import json
import numpy as np

class CommunicationManager:
    
    HOST_IP = '192.168.100.20'

    VIDEO_PORT = 9999
    VIDEO_BUFF_SIZE = 65536
    VIDEO_CLIENT_ADDRESS = ""
    video_client_socket = None

    STATUS_PORT = 8888
    STATUS_BUFF_SIZE = 1024
    STATUS_CLIENT_ADDRESS = ""
    status_client_socket = None

    LOCATION_PORT = 7777
    LOCATION_BUFF_SIZE = 1024
    LOCATION_CLIENT_ADDRESS = ""
    location_client_socket = None


    DISPLAY_PORT = 7777
    DISPLAY_BUFF_SIZE = 1024
    DISPLAY_CLIENT_ADDRESS = ""
    display_client_socket = None


    SMS_PORT = 7777
    SMS_BUFF_SIZE = 1024
    SMS_CLIENT_ADDRESS = ""
    sms_client_socket = None


    used_location_set = set()
    """
    get_parent_info_by_location_index(parent_info, location_indexes, used_indexes):
    
    This static method takes three parameters:
    - parent_info: A NumPy array of parent information.
    - location_indexes: A NumPy array representing location indexes.
    - used_indexes: A set containing the indexes of previously used locations.
    
    It checks for available location indexes, finds the unused indexes, retrieves parent information for those indexes, and returns it.
    """
    @classmethod
    def get_parent_info_by_location_index(cls,parent_info, location_indexes):
        if location_indexes.size == 0:
            print("The 'location_indexes' array is empty.")
            return None

        # Find the unused indexes using NumPy set operations
        unused_indexes = np.setdiff1d(location_indexes, list(cls.used_indexes))

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
     

    @staticmethod
    def send_facial_message(parent_info, selected_indexes):
        selected_parents = parent_info[selected_indexes]
        for parent in selected_parents:
            print("Selected Parent: ", parent)

    """
    reset_used_indexes(used_indexes):
    
    This static method takes a single parameter, used_indexes, which is a set that stores the used indexes. It clears the set of used indexes, effectively resetting it.
    """
    @staticmethod
    def set_host_ip(new_host_ip):
        CommunicationManager.HOST_IP = new_host_ip

    @staticmethod
    def reset_used_indexes(cls):
        cls.used_indexes.clear()

    @classmethod
    def start_video_server(cls):
        cls.video_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.video_client_socket.bind((cls.HOST_IP, cls.VIDEO_PORT))
        print("Establishing a connection with Video Server")
        while True:
        # Initial connection message to the server
            cls.video_client_socket.sendto(b'1', (cls.HOST_IP,cls.VIDEO_PORT))
            data, server_address = cls.video_client_socket.recvfrom(cls.VIDEO_BUFF_SIZE)
            print("Connection established with the Video Server.")


    @classmethod
    def receive_video_data(cls):
        data,server_address =cls.video_client_socket.recvfrom(cls.VIDEO_BUFF_SIZE)
        return data

    @classmethod
    def stop_video_server(cls,):
        cls.video_client_socket.close()


    @classmethod
    def start_status_server(cls):
        cls.status_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Establishing a connection with Status Server")

        # Initial connection message to the server
        cls.status_client_socket.sendto(b'2', (cls.HOST_IP,cls.STATUS_PORT))
        data, server_address = cls.status_client_socket.recvfrom(cls.STATUS_BUFF_SIZE)
        print(f"Connection established with the Status Server.{server_address}")


    @classmethod
    def receive_status_data(cls):
        if cls.status_client_socket is not None:
            data = cls.status_client_socket.recv(cls.STATUS_BUFF_SIZE)
            return data
        else:
            return None

    @classmethod
    def stop_status_server(cls):
        if cls.status_client_socket is not None:
            cls.status_client_socket.close()
            cls.status_client_socket = None  # Reset the socket variable after closing
        else:
            print("Error: Status server not started.")

    @classmethod
    def start_location_server(cls):
        cls.location_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.location_client_socket.bind((cls.HOST_IP, cls.LOCATION_PORT))
        print("Establishing a connection with Location Server")

        while True:
        # Initial connection message to the server
            cls.location_client_socket.sendto(b'3', (cls.HOST_IP,cls.LOCATION_PORT))
            print("Connection established with the Location Server.")

    @classmethod
    def receive_location_data(cls):
        cls.location_client_socket.recvfrom(cls.LOCATION_BUFF_SIZE)

    @classmethod
    def stop_location_server(cls):
        cls.location_client_socket.close()

    @classmethod
    def connect_display_server(cls):
        cls.display_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Establishing a connection with Display Server")
        # Initial connection message to the server
        cls.display_client_socket.connect((cls.HOST_IP,cls.DISPLAY_PORT))
        print("Connection established with the Display Server.")


    @classmethod
    def send_display_data(cls,first_name,last_name,arrival_time):
        data = {'first_name': first_name , 'last_name': last_name, 'arrival_time': arrival_time}
        message = json.dumps(data)
        cls.display_client_socket.send(message.encode())
    

    @classmethod
    def disconnect_display_server(cls):
        cls.display_client_socket.close()


    @classmethod
    def start_sms_server(cls):
        cls.sms_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.sms_client_socket.bind((cls.HOST_IP, cls.SMS_PORT))
        
        print("Establishing a connection with SMS Server")

        while True:
        # Initial connection message to the server
            cls.display_client_socket.sendto(b'5', (cls.HOST_IP,cls.SMS_PORT))
            data, server_address = cls.display_client_socket.recvfrom(cls.SMS_BUFF_SIZE)
            print("Connection established with the SMS Server.")


    @classmethod
    def send_sms_data(cls,message):
        cls.display_client_socket.sendall(message)

    @classmethod
    def stop_display_server(cls):
        cls.sms_client_socket.close()