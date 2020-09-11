from gpiozero import DistanceSensor
from time import sleep



import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import PIL
import adafruit_ssd1306

class myOLED():
    def __init__(self, flipped=False):
        self.flipped = flipped
        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
        self.width = self.disp.width
        self.height = self.disp.height
        self.font = ImageFont.load_default()

        self.image = Image.new("1", (self.width, self.height))
        self.drawing = ImageDraw.Draw(self.image)
        self.text_lines = ["","","",""]

        self.clear()

    def clear(self):
        self.drawing.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.disp.show()

    def set_text(self, line, text, update=True):
        self.text_lines[line] = str(text)
        if update:
            self.clear()
            for i in range(4): self.write_line(i)
            image = self.image
            if self.flipped:
                image = image.transpose(PIL.Image.FLIP_TOP_BOTTOM)
                image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            self.disp.image(image)
            self.disp.show()

    def write_line(self, line):
        text = str(self.text_lines[line])
        padding = -2
        top = padding
        x = 0

        if line == 0: delta = 0
        if line == 1: delta = 8
        if line == 2: delta = 16
        if line == 3: delta = 25

        self.drawing.text((x, top + delta), text, font=self.font, fill=255)


## Main program

sensor = DistanceSensor(echo=26, trigger=19)
display = myOLED()
while True:
    distance = sensor.distance * 100
    print('Distance: ', distance)
    display.set_text(line=0, text=distance, update=True)


    