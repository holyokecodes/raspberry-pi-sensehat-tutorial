from sense_hat import SenseHat
from time import sleep

s = SenseHat()

RED = [255,0,0]
WHITE = [255,255,255]

disarmed = False

# Countdown
for i in range(5,0,-1):
    s.show_letter( str(i) )
    sleep(1)
    for event in s.stick.get_events():
        if (event.action == "pressed"):
            disarmed = True
    if disarmed:
        break

if disarmed:
    s.clear()    
else: # Flashing Explosion
    for i in range(10):
        s.show_letter("X", text_colour=WHITE, back_colour=RED)
        sleep(0.1)
        s.clear()
        sleep(0.1)