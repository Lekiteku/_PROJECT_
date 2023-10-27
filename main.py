import cv2
import numpy as np
import socket
import pickle

# Create a socket to connect to the Azure VM server
server_ip = '20.127.143.111'  # Replace with your Azure VM's public IP address
server_port = 12345  # Choose a port for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((server_ip, server_port))

# Open the local camera
capture = cv2.VideoCapture(0)

frame_count = 0  # Counter to keep track of sent frames

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Serialize the frame
    frame_data = pickle.dumps(frame)
    frame_size = len(frame_data)
    
    # Send the frame size to the server
    client_socket.sendall(frame_size.to_bytes(4, byteorder='big'))
    
    # Log the sent frame size
    print(f'Sent frame size: {frame_size} bytes')

    # Send the frame data
    client_socket.sendall(frame_data)
    
    # Log the number of sent frames
    frame_count += 1
    print(f'Sent frame {frame_count}')

    # Receive confidence data size
    confidence_size = int.from_bytes(client_socket.recv(4), byteorder='big')
    
    # Receive and display the confidence level
    confidence_data = b''
    while len(confidence_data) < confidence_size:
        packet = client_socket.recv(confidence_size - len(confidence_data))
        if not packet:
            break
        confidence_data += packet

    confidence = pickle.loads(confidence_data)
    print(f'Confidence: {confidence}')

    cv2.imshow('Local Video Feed', frame)

    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit the loop
        break

capture.release()
cv2.destroyAllWindows()
