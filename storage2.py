"""
#SERVER SIDE USING COMMUNICATION MANAGER IT WORKS

import socket
import time
import random
import json
from communication import CommunicationManager

def get_sensor_data():
    # Replace this with your actual sensor data retrieval logic
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(40.0, 60.0)
    return temperature, humidity

def start_server():
    CommunicationManager.start_status_server()
    try:
        while True:
            temperature, humidity = get_sensor_data()
            data = {'temperature': temperature, 'humidity': humidity}
            message = json.dumps(data)
            CommunicationManager.send_status_data(message)
            time.sleep(1)  # Adjust the sleep time as needed
    except (ConnectionResetError, BrokenPipeError):
        print("Client disconnected")
    finally:
        CommunicationManager.stop_status_server()

if __name__ == "__main__":
    start_server()

#CLIENT SIDE USING COMMUNICATION MANAGER IT WORKS

import socket
import json

def receive_sensor_data():
    host = '127.0.0.1'  # Replace with the actual IP address of your Raspberry Pi
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((host, port))
    
    try:
        # Initial connection message to the server
        client_socket.send(b'1')
        data, server_address = client_socket.recvfrom(1024)
        print("Connection established with the server.")
        
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Connection closed by the server
            decoded_data = json.loads(data.decode())
            print(f"Temperature: {decoded_data['temperature']:.2f} C, Humidity: {decoded_data['humidity']:.2f}%")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Connection closed")
        client_socket.close()


if __name__ == "__main__":
    receive_sensor_data()

"""


