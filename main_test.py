import multiprocessing
import cv2 as cv
<<<<<<< HEAD
import location as loc



def face_recognition_process(output_queue):
=======


def face_recognition_process():
>>>>>>> MAIN
    # Initialize video capture from the default camera (webcam)
    capture = cv.VideoCapture(0)

    # Load a pre-trained Haar Cascade classifier for face detection
    harr_cascade = cv.CascadeClassifier('harr_face.xml')

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
<<<<<<< HEAD
    print("Facial recognition process is running")
=======
>>>>>>> MAIN

    # Release the video capture
    capture.release()

    # Close the OpenCV display window
    cv.destroyAllWindows()

<<<<<<< HEAD
def location_tracking_process(output_queue):
    while True:
        # Perform location tracking and logging tasks
        lat , long = loc.Location.generate_random_coordinates()
        live_location = (lat,long)
        print(live_location)
    
        print("Location tracking process is running")
        

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # shared_list = manager.list()  # Create a shared list
        # #lock = manager.Lock()  # Create a lock
        # shared_list = []

        # Create two processes, passing the shared list and lock as arguments
        face_process = multiprocessing.Process(target=face_recognition_process,args=output_queue)
        location_process = multiprocessing.Process(target=location_tracking_process,args=ououtput_queue)
=======
def location_tracking_process(shared_list, lock):
    while True:
        # Perform location tracking and logging tasks
        data = "Location data"
        
        # Acquire the lock before modifying the shared list
        lock.acquire()
        shared_list.append(data)
        lock.release()  # Release the lock
        print("Location tracking process is running")

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()  # Create a shared list
        lock = manager.Lock()  # Create a lock

        # Create two processes, passing the shared list and lock as arguments
        face_process = multiprocessing.Process(target=face_recognition_process, args=(shared_list, lock))
        location_process = multiprocessing.Process(target=location_tracking_process, args=(shared_list, lock))
>>>>>>> MAIN

        # Start the processes
        face_process.start()
        location_process.start()

<<<<<<< HEAD
    
=======
        # You can add more logic to control and manage these processes if needed.
        # The lock ensures that only one process can modify the shared list at a time.
>>>>>>> MAIN
