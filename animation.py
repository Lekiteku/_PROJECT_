import time
import board
import busio
import digitalio
import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 0.1

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on the image.
draw = ImageDraw.Draw(image)

# Load the sprite image
sprite = Image.open("icon_28_frames.bmp")
sprite = sprite.convert("1")  # Convert to 1-bit color mode

# Define the sprite size and position
sprite_width, sprite_height = sprite.size
print(f'width is :{sprite_width} height is :{sprite_height}')
  # Height of each sprite frame

# Split the sprite into 28 equal parts
sprite_frames = []
for frame_number in range(28):
    x = frame_number * sprite_frame_width
    y = 0  # Set y to 0 to stack frames horizontally
    frame = sprite.crop((x, y, x + sprite_frame_width, y + sprite_frame_height))
    sprite_frames.append(frame)

# Initialize the font
font = ImageFont.truetype('PixelOperator.ttf', 15)

pointer = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Draw the current frame of the sprite
    draw.bitmap((32, 0), sprite_frames[pointer], fill=255)
    
    # Display image
    oled.image(image)
    oled.show()

    # Wait for a short delay
    time.sleep(LOOPTIME)

    # Update the sprite pointer
    pointer += 1
    if pointer >= 28:
        pointer = 0


