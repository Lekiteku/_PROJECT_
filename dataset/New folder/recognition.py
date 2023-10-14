import cv2 as cv  # Import the OpenCV library as 'cv' for image processing
import os  # Import the 'os' module for file and directory operations
import numpy as np  # Import 'numpy' as 'np' for numerical operations

# Load a Haar Cascade classifier for face detection from the XML file 'harr_face.xml'.
# Make sure the XML file path is correct and contains the necessary face detection model.
haar_cascade = cv.CascadeClassifier('harr_face.xml')

# Define the directory where training images are located.
DIR = r'C:\Users\12143\Documents\PROJECT FINAL YEAR\Face Recognition Code\photos\faces'

# Create an empty list to store the names of the individuals whose faces you want to recognize.
people = []

# Loop through the subdirectories in the specified directory and add their names to the 'people' list.
for i in os.listdir(DIR):
    people.append(i)

# Print the list of people (subdirectories).
print(people)

# Create empty lists to store training data and labels.
feature = []
labels = []

# Define a function 'create_train()' to prepare the training data.
def create_train():
    for person in people:
        path = os.path.join(DIR, person)  # Get the path to the person's directory
        label = people.index(person)  # Assign a label to the person (index of the person's name in 'people' list)

        # Loop through the images in the person's directory.
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)  # Read the image
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)  # Convert the image to grayscale
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)  # Detect faces

            # Loop through the detected faces in the image.
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]  # Extract the region of interest (ROI) where the face is detected
                feature.append(faces_roi)  # Append the face ROI to the 'feature' list
                labels.append(label)  # Append the label to the 'labels' list

# Call the 'create_train()' function to prepare the training data.
create_train()

# Convert the 'feature' and 'labels' lists to NumPy arrays for use in training.
feature = np.array(feature, dtype='object')
labels = np.array(labels)

# Create an LBPH (Local Binary Pattern Histogram) face recognizer using OpenCV.
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the face recognizer using the prepared 'feature' and 'labels' data.
face_recognizer.train(feature, labels)

# Save the trained face recognizer model to a file called 'face_trained.yml'.
face_recognizer.save('face_trained.yml')

# Save the 'feature' and 'labels' NumPy arrays to files 'feature.npy' and 'labels.npy'.
np.save('feature.npy', feature)
np.save('labels.npy', labels)

# Print a message to indicate that the training is finished.
print('Finish training..........')