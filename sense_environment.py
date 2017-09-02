from sense_hat import SenseHat
s = SenseHat()

while True:
    t = s.get_temperature() # Celcius
    p = s.get_pressure()
    h = s.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    
    if t > 28:
        bg = (255,0,0)
    else:
        bg = (0,255,0)
        
    msg = "T: {0} P: {1} H: {2}".format(t,p,h)

    s.show_message(msg, back_colour=bg)