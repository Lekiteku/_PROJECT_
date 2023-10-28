import cv2 as cv
import numpy as np
import socket

# Load a pre-trained Haar Cascade classifier for face detection
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Create a UDP socket for receiving frames from the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a UDP socket for sending processed frames to the client
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port for receiving frames
server_address = ('0.0.0.0', 12345)  # Listen on all available network interfaces

try:
    # Bind the server socket to the address and port
    server_socket.bind(server_address)
    print("Server is listening for connections...")
except socket.error as e:
    print(f"Error binding the server socket: {e}")
    server_socket.close()
    exit(1)

while True:
    # Receive a frame from the client and get the client's address
    try:
        data, client_addr = server_socket.recvfrom(65535)
        print(f"Received a frame from {client_addr}")
    except socket.error as e:
        print(f"Error receiving data: {e}")
        break
    
    # Convert the received data to a NumPy array
    frame = np.frombuffer(data, dtype=np.uint8)

    # Reshape the frame to its original shape
    frame = frame.reshape((480, 640, 3))

    # Print a message to indicate that frame processing has started
    print("Processing the received frame...")

    # Your image processing code (e.g., face detection) goes here

    # Send the processed frame back to the client using the acquired address
    frame_data = frame.tobytes()
    client_addr_with_port = (client_addr[0], 54321)  # Assuming 54321 is the desired port
    send_socket.sendto(frame_data, client_addr_with_port)


    # Check if the 'x' key is pressed to exit the loop
    if cv.waitKey(1) == ord('x'):
        break

# Close both server and send sockets
server_socket.close()
send_socket.close()
