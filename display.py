import time
import board
import busio
import digitalio
import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class DisplayManager:
    # A dictionary to store attendance records
    WIDTH = 128
    HEIGHT = 64
    BORDER = 5
    DISPLAY_RUN_TIME = 10
    # Display Refresh
    LOOPTIME = 1.0
    @staticmethod
    def recordFirst(student_id, student_name):
        print("manijo")

# A dictionary to store attendance records
    @staticmethod
    def displayMessageSuccessful(first_name,last_name,arrival_time):
        digitalioraw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        draw.text((18,0), "REGISTRATION", font=font, fill=255)
        draw.text((24, 16), f"SUCCESSFUL", font=font, fill=255)
        draw.text((0, 32), f"{first_name}", font=font, fill=255)
        draw.text((62, 32), f"{last_name}", font=font, fill=255)
        draw.text((14, 48),f"TIME: {arrival_time}" , font=font, fill=255)
        print("manijo")

    @staticmethod
    def displaySuccessfulRegistration(cls,first_name, last_name, arrival_time):
        i2c = board.I2C()
        oled = adafruit_ssd1306.SSD1306_I2C(cls.WIDTH,cls.HEIGHT, i2c, addr=0x3C, reset=oled_reset)
        print("manijo")
        # Clear display.
        oled.fill(0)
        oled.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a white background
        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

        font = ImageFont.truetype('PixelOperator.ttf', 15)
        #font = ImageFont.load_default()
        start_time = time.time()
        while time.time()-start_time < cls.DISPLAY_RUN_TIME:

        # Draw a black filled box to clear the image.
            DisplayManager.displayMessageSuccessful()
            draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
            first_name = "john "
            last_name = "lbalunye"
            arrival_time =datetime.datetime.now().strftime("%H:%M:%S")
        
        # Pi Stats Display
            draw.text((18,0), "REGISTRATION", font=font, fill=255)
            draw.text((24, 16), f"SUCCESSFUL", font=font, fill=255)
            draw.text((0, 32), f"{first_name}", font=font, fill=255)
            draw.text((62, 32), f"{last_name}", font=font, fill=255)
            draw.text((14, 48),f"TIME: {arrival_time}" , font=font, fill=255)
        # Display image
            oled.image(image)
            oled.show()
            time.sleep(cls.LOOPTIME)
        

