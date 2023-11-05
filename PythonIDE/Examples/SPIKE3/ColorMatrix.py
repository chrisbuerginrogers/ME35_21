import color_matrix
import time
from hub import port

p1 = port.A

colors = {
    "LEGO_BLACK":0,
    "LEGO_MAGENTA":1,
    "LEGO_PURPLE":2,
    "LEGO_BLUE":3,
    "LEGO_AZURE":4,
    "LEGO_TURQUOISE":5,
    "LEGO_GREEN":6,
    "LEGO_YELLOW":7,
    "LEGO_ORANGE":8,
    "LEGO_RED":9,
    "LEGO_WHITE":10,
    "LEGO_DIM_WHITE":11
    }

color_matrix.clear(0)  
(row, col, brightness) = (2, 0, 10)
color_matrix.set_pixel(p1, col, row, (colors['LEGO_RED'], brightness))

time.sleep(1)

for color in range(len(colors)-1):
    col = color % 3
    row = int(color/3) if color < 9 else int((color-9)/3)
    color_matrix.set_pixel(p1, col, row, (color, brightness))
    time.sleep(0.1)

