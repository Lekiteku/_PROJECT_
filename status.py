import time
import json
from communication import CommunicationManager
import subprocess


class StatusManager:
    UPDATE_TIME = 2
    @classmethod
    def receive_status(cls):
        CommunicationManager.start_status_server
        while True:
            CommunicationManager.receive_status_data()
            time.sleep(cls.UPDATE_TIME)

    
