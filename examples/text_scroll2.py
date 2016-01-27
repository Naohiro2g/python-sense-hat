#!/usr/bin/python
import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
msglist = ['Hello world!!', 'One small step for Pi!!', 'Hamamatsu IT Kids', 'IT Robot School', 'Naohiro Tsuji', 'SoniVis Corporation', 'Raspberry Pi 2', 'Astro Pi in the sky...' ]

while True:
    msg = msglist[random.randint(0, len(msglist) - 1)]
    r = random.randint(32, 255)
    g = random.randint(32, 255)
    b = random.randint(32, 255)
    text_colour = (r, g, b)
    scroll_speed = random.randint(0, 10) * 0.01

    sense.show_message(msg, text_colour)
    time.sleep(2)


### show_message
"""
git test

Scrolls a text message from right to left across the LED matrix and at the specified speed, in the specified colour and background colour.

`scroll_speed` | Float | Any floating point number. | The speed at which the text should scroll. This value represents the time paused for between shifting the text to the left by one column of pixels. Defaults to `0.1`
`text_colour` | List | `[R, G, B]` | A list containing the R-G-B (red, green, blue) colour of the text. Each R-G-B element must be an integer between 0 and 255. Defaults to `[255, 255, 255]` white.
`back_colour` | List | `[R, G, B]` | A list containing the R-G-B (red, green, blue) colour of the background. Each R-G-B element must be an integer between 0 and 255. Defaults to `[0, 0, 0]` black / off.
"""
