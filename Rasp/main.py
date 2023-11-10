import socket
import base64
import cv2
import numpy as np
import os


# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_ip = '192.168.0.6'  # Replace with the IP address of the Raspberry Pi
port = 9999
socket_address = (host_ip, port)

# # Define the directory where training images are located.
# DIR = r'dataset'

# # Create an empty list to store the names of the individuals whose faces you want to recognize.
# people = []

# # Loop through the subdirectories in the specified directory and add their names to the 'people' list.
# #for i in os.listdir(DIR):
# #  people.append(i)

# Print the list of people (subdirectories).
#print(people)
haar_cascade = cv2.CascadeClassifier('haar_face.xml')
# face_recognizer = cv2.face_LBPHFaceRecognizer.create()
# face_recognizer.read("face_trained.yml")

print("Establishing a connection with the server...")

connected = False
while True:
    # Initial connection message to the server
    client_socket.sendto(b'1', socket_address)
    data, server_address = client_socket.recvfrom(212992)
    print("Connection established with the server.")

    while True:
        data, server_address = client_socket.recvfrom(212992)
        image_data = base64.b64decode(data)
        nparr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)
        # Draw rectangles around detected faces
        for (x, y, w, h) in face_rect:
            faces_roi = gray[y:y+h, x:x+h]
            
            # Recognize the face and get the label and confidence.
           #label, confidence = face_recognizer.predict(faces_roi)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)
            cv2.rectangle(frame, (x, y-40), (x+w, y), (0, 255, 0), -1)
            #cv2.putText(frame, str(people[label]), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
            #print(f'label = {people[label]} with confidence of {confidence}')

        cv2.imshow('RECEIVING VIDEO', frame)
    
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cv2.destroyAllWindows()
client_socket.close()
