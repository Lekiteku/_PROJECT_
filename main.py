import cv2
import numpy as np
import socket
import pickle

# Create a socket to connect to the Azure VM server
server_ip = 'azure_vm_public_ip'  # Replace with your Azure VM's public IP address
server_port = 12345  # Choose a port for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Open the local camera
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    # Serialize and send the frame to the server
    data = pickle.dumps(frame)
    client_socket.sendall(data)

    # Receive confidence level from the server
    confidence_data = client_socket.recv(1024)  # Adjust the buffer size as needed
    confidence = pickle.loads(confidence_data)
    
    # Display the confidence level
    print(f'Confidence: {confidence}')

    cv2.imshow('Local Video Feed', frame)

    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit the loop
        break

capture.release()
cv2.destroyAllWindows()
