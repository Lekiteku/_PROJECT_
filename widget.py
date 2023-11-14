from typing import Optional
from ui_functions import Ui_Functions
from ui_widget import Ui_MainWindow
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow
import cv2

class Widget(QMainWindow,Ui_MainWindow,Ui_Functions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SBMS")
        self.Exit_Button.clicked.connect(self.buttonClick)
        self.Connection_Button.clicked.connect(self.buttonClick)
        self.Registration_Button.clicked.connect(self.buttonClick)
        self.Facial_Button.clicked.connect(self.buttonClick)
        self.Location_Button.clicked.connect(self.buttonClick)
        self.Display.setAlignment(Qt.AlignCenter)
        self.Display.setFixedSize(640, 480)
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(1000 // 20)

    def updateFrame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.Display.setPixmap(pixmap)

    def closeEvent(self, event):
        self.capture.release()
        cv2.destroyAllWindows()
        event.accept()

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == self.Facial_Button.objectName():
            self.Stacked_Widget.setCurrentWidget(self.Facial_Recognition_Stacked_Widget)
            Ui_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == self.Location_Button.objectName():
            self.Stacked_Widget.setCurrentWidget(self.Proximity_Detection_Stacked_Widget)
            Ui_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == self.Connection_Button.objectName():
            self.Stacked_Widget.setCurrentWidget(self.Connection_Stacked_Widget) # SET PAGE
            Ui_Functions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet())) # SELECT MENU


        if btnName == self.Registration_Button.objectName():
            self.Stacked_Widget.setCurrentWidget(self.Connection_Stacked_Widget) # SET PAGE
            Ui_Functions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(Ui_Functions.selectMenu(btn.styleSheet())) # SELECT MENU


        if btnName == self.Exit_Button:

            print("Save EXIT clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')




"""
import cv2
import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget



class WebcamViewerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Webcam Viewer')
        self.setGeometry(100, 100, 640, 480)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(640, 480)

        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(1000 // 20)

        self.show()

    def updateFrame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.capture.release()
        cv2.destroyAllWindows()
        event.accept()



"""
