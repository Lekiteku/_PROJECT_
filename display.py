import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from os import listdir
import random
import os
from eventcontroller import EventController
from communication import CommunicationManager

class Display:
    OLED_WIDTH = 128
    OLED_HEIGHT = 64
    OLED_BORDER = 5
    FONT_SIZE = 15
    MONOCHROME = True
    LOOPTIME = 0.1
    WELCOME_MESSAGE_TIME = 5
    SPRITE_FRAME_NUMBER = 28
    FILE_NAME = None
    REPLAY_ANIMATION_TIMES = 5
    SPRITE_LIST = []

    @classmethod
    def initialize(cls):
        #CommunicationManager.start_display_server()
        oled_reset = digitalio.DigitalInOut(board.D4)
        i2c = board.I2C()
        cls.oled = adafruit_ssd1306.SSD1306_I2C(cls.OLED_WIDTH, cls.OLED_HEIGHT, i2c, addr=0x3C, reset=oled_reset)
        cls.oled.fill(0)
        cls.oled.show()
        cls.image = Image.new("1", (cls.oled.width, cls.oled.height))
        cls.draw = ImageDraw.Draw(cls.image)
        #cls.font = ImageFont.truetype('PixelOperator.ttf', cls.FONT_SIZE)

    @classmethod
    def create_sprite_frames(cls):
        sprite_folder = "SPRITE"
        bmp_folder = "BMP_FILES"
        sprite_path = os.path.join(sprite_folder, bmp_folder, cls.FILE_NAME)
        sprite = Image.open(cls.FILE_NAME)
        sprite = sprite.convert("1")
        sprite_width, sprite_height = sprite.size
        print(f'width is :{sprite_width} height is :{sprite_height}')
        sprite_frames = []
        for frame_number in range(cls.SPRITE_FRAME_NUMBER):
            x = frame_number * cls.OLED_WIDTH
            y = 0
            frame = sprite.crop((x, y, x + cls.OLED_WIDTH, y + cls.OLED_HEIGHT))
            sprite_frames.append(frame)
        return sprite_frames

    @classmethod
    def run_animation(cls):
        cls.initialize()
        while True:
            count = 1
            cls.choose_random_sprite()
            sprite_frames = cls.create_sprite_frames()
            pointer = 0
            while not EventController.animation_event.is_set():
                cls.draw.rectangle((0, 0, cls.oled.width, cls.oled.height), outline=0, fill=0)
                cls.draw.bitmap((0, 0), sprite_frames[pointer*cls.OLED_WIDTH], fill=255)
                cls.oled.image(cls.image)
                cls.oled.show()
                time.sleep(cls.LOOPTIME)
                pointer += 1
                if pointer >= cls.SPRITE_FRAME_NUMBER:
                    pointer = 0
                    count += 1
                    if count == cls.REPLAY_ANIMATION_TIMES:
                        break

    @classmethod
    def gif_to_bmp(cls, filename: str):
        # Assume filename is just the name of the GIF file, without any path
        gif_path = os.path.join("SPRITE", "GIF_DOWNLOAD", filename)

        # Check if the GIF file exists
        if not os.path.exists(gif_path):
            print(f"GIF file '{filename}' not found in 'SPRITE/GIF_DOWNLOAD' folder.")
            return

        gif = Image.open(gif_path)
        print(f"Size: {gif.size}")
        print(f"Frames: {gif.n_frames}")

        if cls.MONOCHROME:
            output = Image.new("1", (cls.OLED_WIDTH * gif.n_frames, cls.OLED_HEIGHT), 0)
        else:
            output = Image.new("RGB", (cls.OLED_WIDTH * gif.n_frames, cls.OLED_HEIGHT))

        for frame in range(0, gif.n_frames):
            gif.seek(frame)
            resized_frame = gif.resize((cls.OLED_WIDTH, cls.OLED_HEIGHT))
            position = (cls.OLED_WIDTH * frame, 0)
            position = (cls.OLED_HEIGHT * frame, 0)
            output.paste(resized_frame, position)

        if not cls.MONOCHROME:
            output = output.convert("P", colors=8)

        # Create the "Sprite" folder if it doesn't exist
        sprite_folder = "SPRITE"

        # Create the "BMP_Folder" inside the "Sprite" folder if it doesn't exist
        bmp_folder = os.path.join(sprite_folder, "BMP_FILES")
        if not os.path.exists(bmp_folder):
            os.makedirs(bmp_folder)

        # Specify the output file path inside the "BMP_Folder" folder
        output_filename = os.path.join(bmp_folder, f"{filename}_{gif.n_frames}_frames.bmp")
        output.save(output_filename)
        cls.SPRITE_LIST.append((output_filename, gif.n_frames))

        # Navigate back to the original folder
        original_folder = os.path.dirname(os.path.dirname(gif_path))
        print(f"Original Folder: {original_folder}")

    @classmethod
    def set_file_name(cls, filename):
        cls.FILE_NAME = filename

    @classmethod
    def set_sprite_frame_number(cls, frame_number):
        cls.SPRITE_FRAME_NUMBER = frame_number

    @classmethod
    def choose_random_sprite(cls):
        if cls.SPRITE_LIST:
            random_double = random.choice(cls.SPRITE_LIST)
            cls.set_file_name(random_double[0])
            cls.set_sprite_frame_number(random_double[1])
        else:
            print("SPRITE_LIST is empty. No random double to choose.")
            return None

    @classmethod
    def welcome_message(cls):
        while True:
            #first_name , last_name , arrival_time = CommunicationManager.receive_display_data()
            EventController.animation_event.set()
            first_name = "john"
            last_name = "lbalunye"
            arrival_time = "15:25:17"
            # Draw a black filled box to clear the image.
            cls.draw.rectangle((0, 0, cls.OLED_WIDTH, cls.OLED_HEIGHT), outline=0, fill=0)
            # Pi Stats Display
            cls.draw.text((18, 0), "REGISTRATION", font=cls.font, fill=255)
            cls.draw.text((24, 16), "SUCCESSFUL ", font=cls.font, fill=255)
            cls.draw.text((0, 32), f"{first_name}",font=cls.font, fill=255)
            cls.draw.text((64, 32), f"{last_name}",font=cls.font, fill=255)
            cls.draw.text((24, 48), f"{arrival_time}", font=cls.font, fill=255)
            # Display image
            cls.oled.image(cls.image)
            cls.oled.show()
            time.sleep(cls.WELCOME_MESSAGE_TIME)
            EventController.animation_event.clear()



