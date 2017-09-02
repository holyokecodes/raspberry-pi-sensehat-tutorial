from sense_hat import SenseHat
from random import randint
from time import sleep

s = SenseHat()

# Create an array of 64 elements
pixels = [0] * 64

while True:
    # Assign a random color to each of the 64 LEDs
    for i in range(64):
        pixels[i] = [randint(0,255), randint(0,255), randint(0,255)]
    s.set_pixels(pixels)
    sleep(0.1)
