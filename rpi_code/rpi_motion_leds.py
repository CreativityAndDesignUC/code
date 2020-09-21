from gpiozero import MotionSensor
from gpiozero import PWMLED
from time import sleep

pir = MotionSensor('GPIO26')
my_led1 = PWMLED('GPIO6')
my_led2 = PWMLED('GPIO13')

while True:
    print("waiting")
    pir.wait_for_motion()
    print("Motion detected!")


    my_led1.blink(on_time=1, off_time=1, fade_in_time=0.75, fade_out_time=0.75, n=5, background=True)
    sleep(1)
    my_led2.blink(on_time=1, off_time=1, fade_in_time=0.75, fade_out_time=0.75, n=5, background=False)

