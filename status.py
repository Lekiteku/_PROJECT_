import time
import json
from communication import CommunicationManager
import subprocess

class StatusManager:
    UPDATE_TIME = 2

    @classmethod
    def send_status(cls):
        CommunicationManager.start_status_server()
        
        while True:
            # Get system information
            cmd_ip = "hostname -I | cut -d\' \' -f1"
            ip = subprocess.check_output(cmd_ip, shell=True).decode("utf-8").strip()
            cmd_cpu = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
            cpu = subprocess.check_output(cmd_cpu, shell=True).decode("utf-8").strip()
            cmd_mem = "free -m | awk 'NR==2{printf \"%s/%sMB   %.2f%%\", $3,$2,$3*100/$2 }'"
            mem_usage = subprocess.check_output(cmd_mem, shell=True).decode("utf-8").strip()
            cmd_disk = "df -h | awk '$NF==\"/\"{printf \"%d/%dGB   %s\", $3,$2,$5}'"
            disk = subprocess.check_output(cmd_disk, shell=True).decode("utf-8").strip()
            cmd_temp = "vcgencmd measure_temp | cut -f 2 -d '='"
            temp = subprocess.check_output(cmd_temp, shell=True).decode("utf-8").strip()
            
            # Display parameters before creating the data dictionary

            data = {'ip': ip, 'cpu': cpu, 'mem_usage': mem_usage, 'disk': disk, 'temp': temp}
            message = json.dumps(data)

            # Ensure message is a string before encoding
            if isinstance(message, str):
                message = message.encode()

            CommunicationManager.send_status_data(message)
            time.sleep(cls.UPDATE_TIME)


"""
import time
import json
from communication import CommunicationManager
import subprocess

class StatusManager:
    UPDATE_TIME = 2

    @classmethod
    def send_status(cls):
        CommunicationManager.start_status_server()
        while True:
            # Get system information
            cmd_ip = "hostname -I | cut -d\' \' -f1"
            ip = subprocess.check_output(cmd_ip, shell=True).decode("utf-8").strip()
            cmd_cpu = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
            cpu = subprocess.check_output(cmd_cpu, shell=True).decode("utf-8").strip()
            cmd_mem = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
            mem_usage = subprocess.check_output(cmd_mem, shell=True).decode("utf-8").strip()
            cmd_disk = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
            disk = subprocess.check_output(cmd_disk, shell=True).decode("utf-8").strip()
            cmd_temp = "vcgencmd measure_temp | cut -f 2 -d '='"
            temp = subprocess.check_output(cmd_temp, shell=True).decode("utf-8").strip()
            
            # Display parameters before creating the data dictionary
            print(f"IP: {ip}, CPU: {cpu}, Mem Usage: {mem_usage}, Disk: {disk}, Temp: {temp}")

            data = {'ip': ip, 'cpu': cpu, 'mem_usage': mem_usage, 'disk': disk, 'temp': temp}
            message = json.dumps(data)

            # Ensure message is a string before encoding
            if isinstance(message, str):
                message = message.encode()

            # Display the message before sending
            print(f"Sending message: {message}")

            CommunicationManager.send_status_data(message)
            time.sleep(cls.UPDATE_TIME)

"""

