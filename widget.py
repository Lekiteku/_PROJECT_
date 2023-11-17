
from PySide6.QtCore import Qt, QTimer, QThread, Signal,QRegularExpression
from PySide6.QtGui import QImage, QPixmap,QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow
import cv2
import numpy as np
#from ui_functions import Ui_Functions
from ui_widget import Ui_MainWindow
from communication import CommunicationManager
import json
import random
import time


class CameraThread(QThread):
    frame_update = Signal(np.ndarray)
    haar_cascade = cv2.CascadeClassifier('haar_face.xml')

    def run(self):
        capture = cv2.VideoCapture(0)
        while True:
             boolean, frame = capture.read()
             if boolean == True:
        # Convert the frame to grayscale (preferred for face detection)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
                face_rect = self.haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

        # Draw rectangles around detected faces
                for (x, y, w, h) in face_rect:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255), thickness=2)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.frame_update.emit(frame)

class LocationThread(QThread):
    def run(self):
        while True:
            # Your location calculation code goes here
            pass
class StatusThread(QThread):
    status_update = Signal(dict)

    def run(self):
        while True:
            data = CommunicationManager.receive_status_data()
            decoded_data = json.loads(data.decode())
            self.status_update.emit(decoded_data)
         
class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BUMS")

        self.ip_regex = QRegularExpression(
            r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])$"
        )
        
        # Create a validator for the QLineEdit using the IP address regex
        self.ip_validator = QRegularExpressionValidator(self.ip_regex, self.IP_ENTER)
        self.IP_ENTER.setValidator(self.ip_validator)
        self.connectIP.clicked.connect(self.connectButton)
        self.disconnectIP.clicked.connect(self.disconnectButton)
        self.disconnectIP.setDisabled
        self.disconnectIP.setStyleSheet("border:2px solid #35012c;" )
        self.Exit_Button.clicked.connect(self.menuButtonClick)
        self.Connection_Button.clicked.connect(self.menuButtonClick)
        self.Facial_Button.clicked.connect(self.menuButtonClick)
        self.Location_Button.clicked.connect(self.menuButtonClick)
        self.Video_Label.setAlignment(Qt.AlignCenter)
        self.camera_thread = CameraThread()
        self.camera_thread.frame_update.connect(self.updateFrame)
        self.status_thread = StatusThread()
        self.status_thread.status_update.connect(self.updateStatus)
        self.camera_thread.start()
        self.location_thread = LocationThread()
        self.location_thread.start()

    def updateFrame(self, frame):
        # Convert the frame to QImage and display it in Video_Label
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.Video_Label.setPixmap(pixmap)

    def updateStatus(self, decoded_data):
        # Convert the frame to QImage and display it in Video_Label
        self.Temperature_Lcd.setText(decoded_data['temp'])
        self.IP_Lcd.setText(decoded_data['ip'])
        self.Disk_Lcd.setText(decoded_data['disk'])
        self.Cpu_Lcd.setText(decoded_data['cpu'])
        self.Memory_Lcd.setText(decoded_data['mem_usage'])
    
    def updateLocation(self, data):

        pass

    def connectButton(self):

        
        ip = self.IP_ENTER.text()
        #CommunicationManager.set_host_ip(ip)
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText(f"Succesuffully set Bus Unit IP: {ip}")
        #CommunicationManager.start_status_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Status port connected")
        #CommunicationManager.start_sms_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("SMS port connected")
        #CommunicationManager.start_display_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Display port connected")
        # CommunicationManager.start_location_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Location port connected")
        # CommunicationManager.start_video_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Video port connected")
        #self.status_thread.start()
        self.connectIP.setDisabled
        self.disconnectIP.isEnabled
        self.connectIP.setStyleSheet(f"border:2px solid #144552;")
        self.disconnectIP.setStyleSheet("""
            QPushButton {
                background-color: rgb(60, 68, 83);
                border: 2px solid rgb(61, 70, 86);
                color: white; /* Text color */
                padding: 5px; /* Padding around the text */
            }
            QPushButton:hover {
                background-color: rgb(60, 68, 83);
                border: 2px solid rgb(61, 70, 86);
            }
            QPushButton:pressed {
                background-color: rgb(35, 40, 49);
                border: 2px solid rgb(43, 50, 61);
            }
        """)
        pass
    def disconnectButton(self):
        self.connectIP.isEnabled
        self.disconnectIP.setDisabled
        self.disconnectIP.setStyleSheet("border:2px solid #35012c;" )
        self.connectIP.setStyleSheet("""
            QPushButton {
                background-color: rgb(60, 68, 83);
                border: 2px solid rgb(61, 70, 86);
                color: white; /* Text color */
                padding: 5px; /* Padding around the text */
            }
            QPushButton:hover {
                background-color: rgb(60, 68, 83);
                border: 2px solid rgb(61, 70, 86);
            }
            QPushButton:pressed {
                background-color: rgb(35, 40, 49);
                border: 2px solid rgb(43, 50, 61);
            }
        """)
        #CommunicationManager.stop_status_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Status port disconnected")
        #CommunicationManager.stop_sms_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("SMS port disconnected")
        #CommunicationManager.stop_display_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Display port disconnected")
        # CommunicationManager.stop_location_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Location port disconnected")
        # CommunicationManager.stop_video_server()
        self.TERMINAL_PLAINTEXTEDIT.appendPlainText("Video port disconnected")
        #self.status_thread.start()
        self.camera_thread.stop()
        


    def menuButtonClick(self):
        # ... (rest of your buttonClick function remains unchanged)
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == self.Facial_Button.objectName():
            self.stackedWidget.setCurrentWidget(self.Facial_Recognition_Widget)
            #Ui_Functions.resetStyle(self, btnName)
            #btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == self.Location_Button.objectName():
            self.stackedWidget.setCurrentWidget(self.Proximity_Detection_Widget)
            #Ui_Functions.resetStyle(self, btnName)
            #btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == self.Connection_Button.objectName():
            self.stackedWidget.setCurrentWidget(self.Connection_Widget) # SET PAGE
            #Ui_Functions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            #btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == self.Exit_Button:

            print("Save EXIT clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')






