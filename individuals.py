import os
import cv2 as cv
class Person:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.registered = False

    def create_folder(self):
        base_folder = "dataset"
        folder_name = os.path.join(base_folder, f"{self.first_name}_{self.last_name}")

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder for {self.first_name} {self.last_name} in the 'photos' folder.")
       
    def train(self):
        base_folder = "dataset"
        folder_name = os.path.join(base_folder, f"{self.first_name}_{self.last_name}")

    # Initialize video capture from the default camera (webcam)
        capture = cv.VideoCapture(0)

    # Load a pre-trained Haar Cascade classifier for face detection
        harr_cascade = cv.CascadeClassifier('haar_face.xml')

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
                    image_filename = os.path.join(folder_name, f'face_{image_count}.jpg')
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

    # Getter for first_name
    def get_first_name(self):
        return self.first_name

    # Setter for first_name
    def set_first_name(self, first_name):
        self.first_name = first_name

    # Getter for last_name
    def get_last_name(self):
        return self.last_name

    # Setter for last_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    # Getter for gender
    def get_gender(self):
        return self.gender

    # Setter for gender
    def set_gender(self, gender):
        self.gender = gender

class Parent(Person):
    def __init__(self, first_name, last_name, gender, phone_number):
        super().__init__(first_name, last_name, gender)
        self.phone_number = phone_number

    # Getter for phone_number
    def get_phone_number(self):
        return self.phone_number

    # Setter for phone_number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def train(self):
        pass

class Student(Person):
    def __init__(self, first_name, last_name, gender, student_id, parent_first_name, parent_last_name, parent_gender, parent_phone_number):
        super().__init__(first_name, last_name, gender)
        self.student_id = student_id
        self.parent = Parent(parent_first_name, parent_last_name, parent_gender, parent_phone_number)
    
    # Getter for student_id
    def get_student_id(self):
        return self.student_id

    # Setter for student_id
    def set_student_id(self, student_id):
        self.student_id = student_id

    def create_folder(self):
        base_folder = "dataset"
        folder_name = os.path.join(base_folder, f"{self.student_id}")

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder for {self.student_id} in the 'photos' folder.")
            
class SchoolBusStaff(Person):
    def __init__(self, first_name, last_name, gender, staff_id, role):
        super().__init__(first_name, last_name, gender)
        self.staff_id = staff_id
        self.role = role

    # Getter for staff_id
    def get_staff_id(self):
        return self.staff_id

    # Setter for staff_id
    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    # Getter for role
    def get_role(self):
        return self.role

    # Setter for role
    def set_role(self, role):
        self.role = role
