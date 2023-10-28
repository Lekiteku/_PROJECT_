import cv2 as cv
import numpy as np
import socket
import threading

# Function to send video frames to the server
def send_frames():
    # Initialize video capture from the default camera (webcam)
    capture = cv.VideoCapture(0)

    # Create a UDP socket for sending frames to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address and port
    server_address = ('172.191.91.102', 12345)  # Replace 'server_ip_address' with the actual IP address of your Azure VM

    while True:
        # Capture a frame from the webcam
        boolean, frame = capture.read()
        
        if boolean == True:
            # Convert the frame to a NumPy array
            frame_data = frame.tobytes()

            # Send the frame to the server
            client_socket.sendto(frame_data, server_address)

        # Check if the 'x' key is pressed to exit the loop
        if cv.waitKey(1) == ord('x'):
            break

    # Release the video capture
    capture.release()

    # Close the client socket
    client_socket.close()

# Function to display received frames
def display_frames():
    # Create a UDP socket for receiving frames from the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the client address and port for receiving frames
    client_address = ('0.0.0.0', 54321)  # Adjust the port as needed

    # Bind the client socket to the address and port
    client_socket.bind(client_address)

    while True:
        # Receive a frame from the server
        try:
            data, server_address = client_socket.recvfrom(65535)
        except socket.error as e:
            print(f"Error receiving data: {e}")
            break

        # Convert the received data to a NumPy array
        frame = np.frombuffer(data, dtype=np.uint8)

        # Reshape the frame to its original shape
        frame = frame.reshape((480, 640, 3))

        # Display the received frame in a window
        cv.imshow("Received Frame", frame)

        # Check if the 'x' key is pressed to exit the loop
        if cv.waitKey(1) == ord('x'):
            break

    # Close the client socket
    client_socket.close()

# Start the sending and receiving threads
send_thread = threading.Thread(target=send_frames)
display_thread = threading.Thread(target=display_frames)

send_thread.start()
display_thread.start()

# Wait for both threads to finish
send_thread.join()
display_thread.join()

# Close the OpenCV windows
cv.destroyAllWindows()
