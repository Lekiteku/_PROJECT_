# _PROJECT_
This project is designed to set up a face recognition system using Python. 
## Step 1: Create a Dataset
Create a folder named "dataset" to store pictures of the faces you want to recognize. Organize the dataset with subfolders with names of  each person you want to recognize. For example:

---dataset
        ---john_doe
        ---jane_doe
        
## Step 2: Confirm Face Detection
 Run `detection.py` to confirm that the camera can detect faces. If the script doesn't work, make sure to install the required libraries by running `requirements.txt`.
## Step 3: Configure Capture
Open capture.py and update the DIR variable to match the location of your dataset folder created in Step 1. This is where captured images will be stored.
---DIR = "dataset\update here"  # Update this name of person you want to capture
## Step 4: Train the Images
Run training.py to train the images for recognition. This is essential for building the face recognition model.
## Step 5: Face Recognition
Finally, run face_recognition.py to see the final results of your face recognition system.

Please make sure you have all the necessary libraries and dependencies installed as mentioned in the requirements.txt file for the project to work smoothly.Use the command --pip install -r requirements.txt--
