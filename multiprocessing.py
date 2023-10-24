#test multiprocessing
import multiprocessing
import RPi.GPIO as GPIO  # For Raspberry Pi GPIO control
import time

# Set up GPIO pins for the LEDs
LED1_PIN = 17
LED2_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

def control_led1():
    while True:
        GPIO.output(LED1_PIN, GPIO.HIGH)
        time.sleep(1)  # LED1 on for 1 second
        GPIO.output(LED1_PIN, GPIO.LOW)
        time.sleep(1)  # LED1 off for 1 second

def control_led2():
    while True:
        GPIO.output(LED2_PIN, GPIO.HIGH)
        time.sleep(0.5)  # LED2 on for 0.5 seconds
        GPIO.output(LED2_PIN, GPIO.LOW)
        time.sleep(0.5)  # LED2 off for 0.5 seconds

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=control_led1)
    process2 = multiprocessing.Process(target=control_led2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()