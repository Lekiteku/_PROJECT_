import cv2 as cv

# Initialize video capture from the default camera (webcam)
capture = cv.VideoCapture(0)

# Load a pre-trained Haar Cascade classifier for face detection
harr_cascade = cv.CascadeClassifier('haar_face.xml')

# Start an infinite loop for real-time video processing
while True:
    # Capture a frame from the webcam
    boolean, frame = capture.read()
    
    if boolean == True:
        # Convert the frame to grayscale (preferred for face detection)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        face_rect = harr_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

        # Draw rectangles around detected faces
        for (x, y, w, h) in face_rect:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255), thickness=2)

        # Display the frame with detected faces
        cv.imshow("DETECTED FACES", frame)
        
        # Check if the 'x' key is pressed to exit the loop
        if cv.waitKey(20) == ord('x'):
            break

# Release the video capture
capture.release()

# Close the OpenCV display window
cv.destroyAllWindows()
