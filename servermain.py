import cv2 as cv
import numpy as np
import socket
import pickle
import os

# Define the directory where training images are located.
DIR = 'path_to_dataset_directory'  # Update with the correct directory path
people = [d for d in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, d))]

# Load the trained face recognition model
face_recognizer = cv.face_LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# Create a socket to listen for client connections
server_ip = '0.0.0.0'  # Listen on all available network interfaces
server_port = 12345  # Use the same port as the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print('Waiting for client connection...')

client_socket, addr = server_socket.accept()
print(f'Client connected from {addr}')
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    data = client_socket.recv(4096)  # Adjust the buffer size as needed
    frame = pickle.loads(data)

    if frame is not None:
        # Perform face recognition on the frame
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)

        for (x, y, w, h) in face_rect:
            faces_roi = gray[y:y+h, x:x+h]

            # Recognize the face and get the label and confidence.
            label, confidence = face_recognizer.predict(faces_roi)
            confidence_data = pickle.dumps(confidence)

            # Send the confidence level back to the client
            client_socket.sendall(confidence_data)

server_socket.close()
