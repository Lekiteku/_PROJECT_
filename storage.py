"""
#SERVER MAIN

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
WIDTH = 500
while True:
    data, client_address = server_socket.recvfrom(BUFF_SIZE)
    if data == b'1':
        print('Connection established with', client_address)
        break
while True:
    frame = picam.capture_array()
    # Convert the frame to JPEG format
    frame = imutils.resize(frame, width=WIDTH)
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



#ANIMATION

import time
import board
import busio
import digitalio
import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 0.1

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on the image.
draw = ImageDraw.Draw(image)

# Load the sprite image
sprite = Image.open("icon_28_frames.bmp")
sprite = sprite.convert("1")  # Convert to 1-bit color mode

# Define the sprite size and position
sprite_width, sprite_height = sprite.size
print(f'width is :{sprite_width} height is :{sprite_height}')
  # Height of each sprite frame

# Split the sprite into 28 equal parts
sprite_frames = []
for frame_number in range(28):
    x = frame_number * sprite_frame_width
    y = 0  # Set y to 0 to stack frames horizontally
    frame = sprite.crop((x, y, x + sprite_frame_width, y + sprite_frame_height))
    sprite_frames.append(frame)

# Initialize the font
font = ImageFont.truetype('PixelOperator.ttf', 15)

pointer = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Draw the current frame of the sprite
    draw.bitmap((32, 0), sprite_frames[pointer], fill=255)
    
    # Display image
    oled.image(image)
    oled.show()

    # Wait for a short delay
    time.sleep(LOOPTIME)

    # Update the sprite pointer
    pointer += 1
    if pointer >= 28:
        pointer = 0


#GIF2BMPCONTROLLER

from os import listdir
from PIL import Image

OUTPUT_SIZE = (128,64) # The output size of each frame (or tile or Sprite) of the animation
MONOCHROME = True # Do you want the output file to be b/w?

for file in listdir():
    if file.endswith('.gif'):
        gif = Image.open(file)
        print(f"Size: {gif.size}")
        print(f"Frames: {gif.n_frames}")

        if MONOCHROME:
            output = Image.new("1", (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]), 0)
        else:
            output = Image.new("RGB", (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]))

        output_filename = f"icon2_{gif.n_frames}_frames.bmp"

        for frame in range(0,gif.n_frames):
            gif.seek(frame)
            extracted_frame = gif.resize(OUTPUT_SIZE)
            position = (OUTPUT_SIZE[0]*frame, 0)
            output.paste(extracted_frame, position)

        if not MONOCHROME:
            output = output.convert("P", colors = 8)
        output.save(output_filename)

        
        
#MAIN

import socket
import base64
import cv2
import numpy as np
import os


# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_ip = '192.168.0.6'  
port = 9999
socket_address = (host_ip, port)

# Define the directory where training images are located.
DIR = r'dataset'

# Create an empty list to store the names of the individuals whose faces you want to recognize.
people = []

# Loop through the subdirectories in the specified directory and add their names to the 'people' list.
for i in os.listdir(DIR):
    people.append(i)

# Print the list of people (subdirectories).
print(people)
haar_cascade = cv2.CascadeClassifier('haar_face.xml')
face_recognizer = cv2.face_LBPHFaceRecognizer.create()
face_recognizer.read("face_trained.yml")

print("Establishing a connection with the server...")

connected = False
while True:
    # Initial connection message to the server
    client_socket.sendto(b'1', socket_address)
    data, server_address = client_socket.recvfrom(65536)
    print("Connection established with the server.")

    while True:
        data, server_address = client_socket.recvfrom(65536)
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
            label, confidence = face_recognizer.predict(faces_roi)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)
            cv2.rectangle(frame, (x, y-40), (x+w, y), (0, 255, 0), -1)
            cv2.putText(frame, str(people[label]), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
            print(f'label = {people[label]} with confidence of {confidence}')

        cv2.imshow('RECEIVING VIDEO', frame)
    
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cv2.destroyAllWindows()
client_socket.close()

"""

