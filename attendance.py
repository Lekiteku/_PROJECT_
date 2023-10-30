import numpy as np
from display import DisplayManager
import datetime


class AttendanceManager:
    # Sets to store used indices
    used_indices_location = set()
    used_indices_facial = set()
    attendace_record = []
    CONFIDENCE = 50  # Default confidence value
    def record_attendance(cls, student_id, student_name):
        # Record the attendance with student's name and current time
        current_time = datetime.datetime.now()
        attendance_record = {
            "student_id": student_id,
            "student_name": student_name,
            "attendance_time": current_time
        }
        cls.attendance_records.append(attendance_record)

    @staticmethod
    def recordAttendance(cls, label, data_array):
        if label in cls.used_indices:
            print(f"Index {label} is already in use.")
        else:
            cls.used_indices.add(label)
            print(f"Index {label} added to the used indices.")
        
    @staticmethod
    def register(cls,label, confidence):
        if confidence >= cls.CONFIDENCE:
            AttendanceManager.check_if_recoded(label)
            print("Yes, registered")
        else:
            return None

    @classmethod
    def check_if_recoded(cls,label):
        if label in cls.used_indices:
            return None
        else:
            cls.used_indices.add(label)

    @classmethod
    def reset_used_location(cls):
        cls.used_indices_location.clear()
        print("Used indices for location have been reset.")

    @classmethod
    def reset_used_facial(cls):
        cls.used_indices_facial.clear()
        print("Used indices for facial recognition have been reset.")

    @classmethod
    def set_confidence(cls, new_confidence):
        if isinstance(new_confidence, int):
            cls.CONFIDENCE = new_confidence
            print(f"CONFIDENCE has been set to {new_confidence}")
        else:
            print("Invalid data type. CONFIDENCE must be an integer.")

    @classmethod
    def reset_confidence(cls):
        cls.CONFIDENCE = 50  # Reset CONFIDENCE to its default value
        print("CONFIDENCE has been reset to its default value.")
