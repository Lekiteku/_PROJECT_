import socket
import json

class CommunicationManager:
    HOST_IP = '0.0.0.0'

    VIDEO_PORT = 9999
    VIDEO_BUFF_SIZE = 65536
    VIDEO_CLIENT_ADDRESS = ""
    video_server_socket = None

    STATUS_PORT = 8888
    STATUS_BUFF_SIZE = 1024
    STATUS_CLIENT_ADDRESS = ""
    status_server_socket = None

    LOCATION_PORT = 7777
    LOCATION_BUFF_SIZE = 1024
    LOCATION_CLIENT_ADDRESS = ""
    location_server_socket = None


    DISPLAY_PORT = 7777
    DISPLAY_BUFF_SIZE = 1024
    DISPLAY_CLIENT_ADDRESS = ""
    display_server_socket = None


    SMS_PORT = 7777
    SMS_BUFF_SIZE = 1024
    SMS_CLIENT_ADDRESS = ""
    sms_server_socket = None

    @classmethod
    def start_video_server(cls):
        cls.video_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.video_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, cls.VIDEO_BUFF_SIZE)
        cls.video_server_socket.bind((cls.HOST_IP, cls.VIDEO_PORT))
        print(f"Video Server listening on {cls.HOST_IP}:{cls.VIDEO_PORT}")
        while True:
            data, client_address = cls.video_server_socket.recvfrom(cls.VIDEO_BUFF_SIZE)
            if data == b'1':
                print('Video connection established with', client_address)
                cls.VIDEO_CLIENT_ADDRESS = client_address
                break

    @classmethod
    def send_video_data(cls, message):
        cls.video_server_socket.sendto(message, cls.VIDEO_CLIENT_ADDRESS)

    @classmethod
    def stop_video_server(cls,):
        cls.video_server_socket.close()

    @classmethod
    def start_status_server(cls):
        cls.status_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.status_server_socket.bind((cls.HOST_IP, cls.STATUS_PORT))
        print(f"Status Server listening on {cls.HOST_IP}:{cls.STATUS_PORT}")

        while True:
            data, client_address = cls.status_server_socket.recvfrom(cls.STATUS_BUFF_SIZE)
            if data == b'2':
                print('Status connection established with', client_address)
                cls.STATUS_CLIENT_ADDRESS = client_address
                break

    @classmethod
    def send_status_data(cls, message):
        cls.status_server_socket.sendto(message.encode(), cls.STATUS_CLIENT_ADDRESS)


    @classmethod
    def stop_status_server(cls, message):
        cls.status_server_socket.close()


    @classmethod
    def start_location_server(cls):
        cls.location_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.location_server_socket.bind((cls.HOST_IP, cls.LOCATION_PORT))
        print(f"Location Server listening on {cls.HOST_IP}:{cls.LOCATION_PORT}")

        while True:
            data, client_address = cls.location_server_socket.recvfrom(cls.LOCATION_BUFF_SIZE)
            if data == b'3':
                print('Location connection established with', client_address)
                cls.LOCATION_CLIENT_ADDRESS = client_address
                break

    @classmethod
    def send_location_data(cls, message):
        cls.location_server_socket.sendto(message, cls.LOCATION_CLIENT_ADDRESS)

    @classmethod
    def stop_location_server(cls):
        cls.location_server_socket.close()

    @classmethod
    def start_display_server(cls):
        cls.display_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.display_server_socket.bind((cls.HOST_IP, cls.DISPLAY_PORT))
        cls.status_server_socket.listen(1)

        print(f"Location Server listening on {cls.HOST_IP}:{cls.DISPLAY_PORT}")
        conn, addr = cls.status_server_socket.accept()
        with conn:
            print('Status connection established with', addr)
            cls.STATUS_CLIENT_ADDRESS = addr


    @classmethod
    def receive_display_data(cls):
        data = cls.display_server_socket.recv(cls.DISPLAY_BUFF_SIZE)
        return data
    

    @classmethod
    def stop_display_server(cls):
        cls.display_server_socket.close()



    @classmethod
    def start_sms_server(cls):
        cls.sms_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.sms_server_socket.bind((cls.HOST_IP, cls.SMS_PORT))
        
        print(f"Location Server listening on {cls.HOST_IP}:{cls.SMS_PORT}")

        while True:
            data, client_address = cls.sms_server_socket.recvfrom(cls.SMS_BUFF_SIZE)
            if data == b'1':
                print('Location connection established with', client_address)
                cls.SMS_CLIENT_ADDRESS = client_address
                break

    @classmethod
    def receive_sms_data(cls):
        data = cls.sms_server_socket.recv(cls.DISPLAY_BUFF_SIZE)
        return data



    @classmethod
    def stop_display_server(cls):
        cls.sms_server_socket.close()