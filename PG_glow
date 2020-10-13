import time
import math
import neopixel
import board
import adafruit_lis3dh
import busio
 
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_8_G


 
def get_acceleration():
    x, y, z = lis3dh.acceleration
    s = x**2 + y**2 + z**2
    return s
    

class wave:
    def __init__(self):
        self.time = 0
        self.value = 0
    
    def step(self, time_step, frequency):
        self.time = self.time + time_step * frequency
        self.value = math.sin(2 * math.pi * self.time)
        self.value =  (self.value + 1) / 2
        return self.value
    


class integrator:
    def __init__(self):
        self.value = 0
        self.max = 1
        self.min = 0

    
    def update(self, value):
        self.value = self.value + value
        self.value = self.value * (1 - leak_rate)
        if self.value > self.max: self.value = self.max
        if self.value < self.min: self.value = self.min
        return self.value
    
    
class glow:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
        self.integrator = integrator()
        self.wave = wave()
    
    def activate(self, value, time_step):
        value = self.integrator.update(value)
        frequency = value * (max_freq - min_freq) + min_freq
        value = self.wave.step(time_step, frequency)
        intensity = int(value * 255)
        self.pixels.fill((0,0,intensity))
        return frequency, intensity
    
    
max_freq = 30
min_freq = 0.5
leak_rate = 0.01
acceleration_threshold = 250
activation = 0.025
delay = 0.025


g = glow()
while True:
    t0 = time.time()
    acceleration = get_acceleration()
    if acceleration > acceleration_threshold:
        frequency, intensity = g.activate(activation, delay)
    else:
        frequency, intensity  = g.activate(0, delay)
    print(acceleration, frequency, intensity)
    time.sleep(delay)
    t1 = time.time()
    #delta = t1 - t0
    #print(delta)
    
