from sense_hat import SenseHat

s = SenseHat()
s.set_rotation(90)

while True:
    deg = s.get_compass()
    print(deg)
    if deg < 45 or deg > 315:
        s.show_letter("N")
    elif deg < 135:
        s.show_letter("E")
    elif deg < 225:
        s.show_letter("S")
    else:
        s.show_letter("W")
        