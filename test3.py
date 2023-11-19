from communication import CommunicationManager
import time

CommunicationManager.connect_display_server()
#first_name = input("Enter first name: ")
#last_name = input("Enter last name: ")
#arrival_time = input("Enter arrival time: ")
time.sleep(10)
first_name = "manijo"
last_name ="leiyagu"
arrival_time ="12:23:43"
CommunicationManager.send_display_data(first_name,last_name,arrival_time)