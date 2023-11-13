import socket
import threading

class CommunicationManager:

    HOST_IP = '192.168.0.6'

    VIDEO_PORT = 9999
    VIDEO_BUFF_SIZE = 65536
    VIDEO_CLIENT_ADDRESS = ""
    video_server_socket = None

    STATUS_PORT = 8888
    STATUS_BUFF_SIZE = 1024
    STATUS_CLIENT_ADDRESS = ""
    status_server_socket = None

    
    LOCATION_PORT = 7777
    LOCATION_PORT_BUFF_SIZE = 1024
    LOCATION_CLIENT_ADDRESS = ""
    location_server_socket = None

    @classmethod
    def start_video_server(cls):
        cls.video_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.video_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, cls.VIDEO_BUFF_SIZE)
        cls.video_server_socket.bind((cls.HOST,cls.VIDEO_PORT))

        print(f"Video Server listening on {cls.HOST_IP}:{cls.VIDEO_PORT}")

        while True:
            data, client_address = cls.video_server_socket.recvfrom(cls.VIDEO_BUFF_SIZE)
            if data == b'1':
                print('Video connection established with', client_address)
                cls.VIDEO_CLIENT_ADDRESS = client_address
                break
    @classmethod
    def send_video_data(cls,message):
        cls.video_server_socket.sendto(message,cls.CLIENT_ADDRESS)

    @classmethod
    def start_status_server(cls):
        cls.status_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.status_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, cls.STATUS_BUFF_SIZE)
        cls.status_server_socket.bind((cls.HOST_IP, cls.STATUS_PORT))
        print(f"Status Server listening on {cls.HOST_IP}:{cls.STATUS_CLIENT_ADDRESS}")

        while True:
            data, client_address = cls.video_server_socket.recvfrom(cls.VIDEO_BUFF_SIZE)
            if data == b'2':
                print('Status connection established with', client_address)
                cls.VIDEO_CLIENT_ADDRESS = client_address
                break
    
    @classmethod
    def send_status_data(cls,message):
        cls.status_server_socket.sendto(message,cls.STATUS_CLIENT_ADDRESS)

    @classmethod
    def start_location_server(cls):
        cls.location_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.location_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, cls.LOCATION_BUFF_SIZE)
        cls.location_server_socket.bind((cls.HOST,cls.LOCATION_PORT))

        print(f"Video Server listening on {cls.HOST_IP}:{cls.LOCATION_PORT}")

        while True:
            data, client_address = cls.video_server_socket.recvfrom(cls.LOCATION_BUFF_SIZE)
            if data == b'1':
                print('Video connection established with', client_address)
                cls.LOCATION_CLIENT_ADDRESS = client_address
                break
    @classmethod
    def send_location_data(cls,message):
        cls.location_server_socket.sendto(message,cls.CLIENT_ADDRESS)

