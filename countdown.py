from sense_hat import SenseHat
from time import sleep

s = SenseHat()

RED = [255,0,0]
WHITE = [255,255,255]

# Countdown
for i in range(5,0,-1):
    s.show_letter( str(i) )
    sleep(1)

# Flashing Explosion
for i in range(6):
    s.show_letter("X", text_colour=WHITE, back_colour=RED)
    sleep(0.1)
    s.clear()
    sleep(0.1)
