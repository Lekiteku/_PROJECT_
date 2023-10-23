import cv2 as cv  # Import the OpenCV library as 'cv' for image processing
import numpy as np  # Import 'numpy' as 'np' for numerical operations
import os  # Import the 'os' module for file and directory operations

# Define the directory where training images are located.
DIR = r'.\dataset'

# Create an empty list to store the names of the individuals whose faces you want to recognize.
people = []

# Loop through the subdirectories in the specified directory and add their names to the 'people' list.
for i in os.listdir(DIR):
    people.append(i)

# Print the list of people (subdirectories).
print(people)

# Create a LBPH (Local Binary Pattern Histogram) face recognizer.
face_recognizer = cv.face_LBPHFaceRecognizer.create()

# Load the trained face recognition model from 'face_trained.yml'.
face_recognizer.read("face_trained.yml")

# Open a video capture from the default camera (index 0).
capture = cv.VideoCapture(0)

# Load a Haar Cascade classifier for face detection from the XML file 'harr_face.xml'.
harr_cascade = cv.CascadeClassifier('haar_face.xml')

# Create an infinite loop to capture and recognize faces in real-time video.
while True:
    boolean, frame = capture.read()  # Read a frame from the video capture
    
    if boolean == True:  # Check if the frame was read successfully
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convert the frame to grayscale
        
        # Detect faces in the grayscale frame using the Haar Cascade classifier.
        face_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)
        
        # Loop through the detected faces and draw rectangles and labels.
        for (x, y, w, h) in face_rect:
            faces_roi = gray[y:y+h, x:x+h]
            
            # Recognize the face and get the label and confidence.
            label, confidence = face_recognizer.predict(faces_roi)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)
            cv.rectangle(frame, (x, y-40), (x+w, y), (0, 255, 0), -1)
            cv.putText(frame, str(people[label]), (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), thickness=2)
            print(f'label = {people[label]} with confidence of {confidence}')

        # Display the frame with detected faces.
        cv.imshow("DETECTED FACES", frame)
        
        # Check for the 'x' key press to exit the while loop.
        if cv.waitKey(20) == ord('x'):
            break

# Release the video capture and close any open windows.
capture.release()
cv.destroyAllWindows()
