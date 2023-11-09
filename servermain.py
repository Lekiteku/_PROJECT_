import socket
import time
import base64
from picamera2 import Picamera2
import cv2
import imutils

picam = Picamera2()
picam.preview_configuration.main.size = (640, 480)
picam.preview_configuration.main.format = "RGB888"
picam.preview_configuration.align()
picam.configure("preview")
picam.start()

# Set up the server socket for sending images
BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
host_ip = '192.168.0.x'  # Replace with the PC's IP address
port = 9999
socket_address = (host_ip, port)
server_socket.bind(server_socket)
print("Listening at :", socket_address)
WIDTH = 480
HEIGHT = 640
while True:
    data, client_address = server_socket.recvfrom(BUFF_SIZE)
    if data == b'1':
        print('Connection established with', client_address)
        break
while True:
    frame = picam.capture_array()
    # Convert the frame to JPEG format
    frame = imutils.resize(frame, width=WIDTH, height=HEIGHT)
    encoded, buffer= cv2.imencode('.jpg', frame,[cv2.IMWRITE_WEBP_QUALITY,80])
    message = base64.b64encode(buffer)
    server_socket.sendto(message,client_address)
    cv2.imshow('TRANSMITTING VIDEO',frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        server_socket.close()
        break

cv2.destroyAllWindows()
server_socket.close()

