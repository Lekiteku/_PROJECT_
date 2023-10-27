import cv2 as cv
import os
import numpy as np

# Load Haar Cascade for face detection
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Define the directory where training images are located
DIR = r'dataset'

# Create an empty list to store the names of individuals
people = sorted(os.listdir(DIR))  # Ensure alphabetical sorting

# Create empty lists to store training data and labels
features = []
labels = []

# Define a function 'create_train()' to prepare the training data
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)

            if img_array is not None:
                # Detect faces in the image
                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

                for (x, y, w, h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    # Resize to a standard size (e.g., 128x128) and normalize pixel values
                    faces_roi = cv.resize(faces_roi, (128, 128)) / 255.0

                    features.append(faces_roi)
                    labels.append(label)

# Call the 'create_train()' function to prepare the training data
create_train()

# Convert the 'features' and 'labels' lists to NumPy arrays for training
features = np.array(features, dtype=np.float32)
labels = np.array(labels)

# Create LBPH (Local Binary Pattern Histogram) face recognizer
face_recognizer = cv.face_LBPHFaceRecognizer_create()

# Train the face recognizer using the prepared 'features' and 'labels' data
face_recognizer.train(features, labels)

# Save the trained face recognizer model to a file called 'face_trained.yml'
face_recognizer.save('face_trained.yml')

# Save the 'features' and 'labels' NumPy arrays to files 'features.npy' and 'labels.npy'
np.save('features.npy', features)
np.save('labels.npy', labels)

# Print a message to indicate that the training is finished
print('Training completed.')
