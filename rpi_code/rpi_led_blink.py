from gpiozero import PWMLED

my_led = PWMLED('GPIO26')

# blink 5 times
print('blink')
my_led.blink(on_time=1, off_time=1, fade_in_time=0.75, fade_out_time=0.75, n=5) 