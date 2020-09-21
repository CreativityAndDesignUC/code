from gpiozero import Servo
from time import sleep

my_servo = Servo('gpio26',min_pulse_width=900/1000000,
                 max_pulse_width=2100/1000000,
                 frame_width=100/1000)

while True:
    my_servo.min()
    sleep(2)
    my_servo.max()
    sleep(2)