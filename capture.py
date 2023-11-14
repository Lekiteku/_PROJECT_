import base64
from picamera2 import Picamera2
import cv2
import imutils
from communication import CommunicationManager

class CameraStreamer:
    CAM_WIDTH = 640
    CAM_HEIGHT = 480
    WIDTH = 500

    
    @classmethod
    def initialize_camera(cls):
        CommunicationManager.start_video_server()
        try:
            picam = Picamera2()
            picam.preview_configuration.main.size = (cls.CAM_WIDTH, cls.CAM_HEIGHT)
            picam.preview_configuration.main.format = "RGB888"
            picam.preview_configuration.align()
            picam.configure("preview")
            picam.start()    
            return picam
        except Exception as e:
                print(f"Error initializing camera: {e}")
                return None

    @classmethod
    def send_images(cls):
        picam = cls.initialize_camera()
        try:
            while True:
                frame = picam.capture_array()
                frame = imutils.resize(frame, width=cls.WIDTH)
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_WEBP_QUALITY, 80])
                message = base64.b64encode(buffer)
                CommunicationManager.send_video_data(message)
        except Exception as e:
            print(f"Error sending frame: {e}")
        finally:
            picam.stop()  # Stop the camera to release resources
            CommunicationManager.stop_video_server()
