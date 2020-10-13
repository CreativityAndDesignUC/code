import time
import board
import touchio
import neopixel

#You may need to restart your code/board after changing the attached item because 
# the capacitive touch code 'calibrates' based on what it sees when it first starts up.
 
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_TX = touchio.TouchIn(board.TX)
 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    if touch_A1.value:
        print("A1 touched!")
        pixels[0] = (250, 0, 0)
    else:
        pixels[0] = (0, 0, 0)

    pixels.show()
    time.sleep(0.01)
