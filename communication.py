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
    dispay_conn = None


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
    def send_location_data(cls, message):
        cls.location_server_socket.sendto(message.encode(), cls.LOCATION_CLIENT_ADDRESS)

    @classmethod
    def stop_location_server(cls):
        cls.location_server_socket.close()

   
    @classmethod
    def start_sms_server(cls):
        cls.sms_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.sms_server_socket.bind((cls.HOST_IP, cls.SMS_PORT))
        print(f"SMS Server listening on {cls.HOST_IP}:{cls.SMS_PORT}")
        cls.sms_server_socket.listen(1)

    @classmethod
    def receive_sms_data(cls):
        client_sms_port, client_sms_address = cls.display_server_socket.accept()
        data = client_sms_port.recv(cls.DISPLAY_BUFF_SIZE)
        decoded_data = json.loads((data.decode()))
        first_name = decoded_data['first_name']
        last_name = decoded_data['last_name']
        arrival_time = decoded_data['first_name']
        return first_name,last_name,


    @classmethod
    def stop_sms_server(cls):
        cls.sms_server_socket.close()

    @classmethod
    def start_display_server(cls):
        cls.display_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.display_server_socket.bind((cls.HOST_IP, cls.DISPLAY_PORT))
        print(f"Display Server listening on {cls.HOST_IP}:{cls.STATUS_PORT}")
        cls.display_server_socket.listen(1)


    @classmethod
    def receive_display_data(cls):
        client_display_port, client_display_address = cls.display_server_socket.accept()
        data = client_display_port.recv(cls.DISPLAY_BUFF_SIZE)
        decoded_data = json.loads((data.decode()))
        first_name = decoded_data['first_name']
        last_name = decoded_data['last_name']
        arrival_time = decoded_data['first_name']
        return first_name,last_name,arrival_time
    

    @classmethod
    def stop_display_server(cls):
        cls.display_server_socket.close()
