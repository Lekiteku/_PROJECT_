import time
import json
from communication import CommunicationManager
import subprocess

class StatusManager:
    UPDATE_TIME = 2

    @classmethod
    def receive_status(cls):
        CommunicationManager.start_status_server()
        count = 0
        while True:
            count += 1
            data = CommunicationManager.receive_status_data()
            decoded_data = json.loads(data)
            print(f"IP: {decoded_data['ip']}, CPU: {decoded_data['cpu']}, Mem Usage: {decoded_data['mem_usage']}, Disk: {decoded_data['disk']}, Temp: {decoded_data['temp']}")
            if count == 10:
                break
        CommunicationManager.stop_status_server()
