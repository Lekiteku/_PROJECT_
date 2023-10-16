import cv2 as cv
import os 

DIR = r'.\dateset\faces\manijo'

# Initialize video capture from the default camera (webcam)
capture = cv.VideoCapture(0)

# Load a pre-trained Haar Cascade classifier for face detection
harr_cascade = cv.CascadeClassifier('harr_face.xml')

# Counter to keep track of the number of captured face images.
image_count = 0        

# Start an infinite loop for real-time video processing           
while True:
    # Capture a frame from the webcam
    boolean, frame = capture.read()
    
    if boolean == True:
        #Convert the frame to grayscale (preferred for face detection)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        face_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)


        # Draw rectangles around detected faces
        for (x, y, w, h) in face_rect:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255), thickness=2)

        key = cv.waitKey(1)
        if key == 32:  # Press 'Space' key to capture a face image.
            image_count += 1
            face_roi = frame[y:y + h, x:x + w]
            image_filename = os.path.join(DIR, f'face_{image_count}.jpg')
            cv.imwrite(image_filename, face_roi)
            cv.putText(frame, str(image_count), (x, y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
            print(f"Face {image_count} captured and saved as {image_filename}")
            if image_count == 50                   :
                break

        # Display the frame with detected faces
        cv.imshow("DETECTED FACES", frame)
        # Check for user input to exit the loop.
        key = cv.waitKey(1)
        if key == 27:  # Press 'Esc' key to exit the loop.
            break
        
        # Check if the 'x' key is pressed to exit the loop
        if cv.waitKey(20) == ord('x'):
            break

# Release the video capture
capture.release()

# Close the OpenCV display window
cv.destroyAllWindows()

