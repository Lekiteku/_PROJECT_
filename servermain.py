import cv2
import numpy as np
import socket
import queue
import threading
import time
import struct

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to an IP and port to receive video frames
receiver_ip = '0.0.0.0'  # Listen on all available network interfaces
receiver_port = 12345  # Use the same port as in the sender

try:
    client_socket.bind((receiver_ip, receiver_port))
except Exception as e:
    print(f"Error binding to socket: {e}")
    exit(1)

# Create a VideoWriter to decode and display the frames
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('receiver_output.mp4', fourcc, 20.0, (640, 480))  # Adjust as needed

# Initialize a jitter buffer
frame_buffer = queue.PriorityQueue()

def process_frame(frame_data, timestamp):
    frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
    out.write(frame)
    cv2.imshow("Received", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return

while True:
    try:
        data, addr = client_socket.recvfrom(65535)  # Adjust buffer size if needed
    except Exception as e:
        print(f"Error receiving data: {e}")
        continue

    try:
        # Deserialize the frame from bytes
        timestamp, frame_data = data[:8], data[8:]
        frame_timestamp = struct.unpack('d', timestamp)[0]

        # Place the frame in the buffer with its timestamp as the priority
        frame_buffer.put((frame_timestamp, frame_data))
    except Exception as e:
        print(f"Error processing frame: {e}")
        continue

    # Process frames in the buffer
    current_time = time.time()
    while not frame_buffer.empty():
        frame_timestamp, frame_data = frame_buffer.get()
        frame_age = current_time - frame_timestamp

        # Process the frame if it's not too old (adjust the threshold as needed)
        if frame_age < 1.0:
            process_frame(frame_data, timestamp)
        else:
            print(f"Discarded an old frame (age: {frame_age:.2f} seconds)")

# Release resources when done
out.release()
cv2.destroyAllWindows()
