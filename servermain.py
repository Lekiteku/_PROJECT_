import socket
import cv2
import numpy as np

# Create a socket to listen for client connections
server_ip = '0.0.0.0'  # Listen on all available network interfaces
server_port = 12345  # Use the same port as the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print('Waiting for client connection...')

while True:
    # Receive the data size indicating the frame length
    data_size = int.from_bytes(server_socket.recv(4), byteorder='big')

    # Receive the frame data
    data = b''
    while len(data) < data_size:
        packet = server_socket.recv(data_size - len(data))
        if not packet:
            break
        data += packet

    # Log the received frame size
    print(f'Received frame size: {data_size} bytes')

    # Convert binary data to a NumPy array
    frame_data = np.frombuffer(data, dtype=np.uint8)

    # Decode the JPEG image
    frame = cv2.imdecode(frame_data, cv2.IMREAD_COLOR)

    if frame is not None:
        # Optionally, you can save or process the JPEG image here
        cv2.imwrite('received_image.jpg', frame)  # Save the received image

        # Perform any further processing or display as needed
        cv2.imshow('Received Image', frame)
        cv2.waitKey(0)

# Don't forget to release the OpenCV window when done
cv2.destroyAllWindows()
