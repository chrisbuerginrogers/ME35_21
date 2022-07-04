import color_matrix
import port,time

p1 = port.PORTE

colors = {
    0:"LEGO_BLACK",
    1:"LEGO_MAGENTA",
    2:"LEGO_PURPLE",
    3:"LEGO_BLUE",
    4:"LEGO_AZURE",
    5:"LEGO_TURQUOISE",
    6:"LEGO_GREEN",
    7:"LEGO_YELLOW",
    8:"LEGO_ORANGE",
    9:"LEGO_RED",
    10:"LEGO_WHITE",
    11:"LEGO_DIM_WHITE",
    }

color_matrix.clear(4)  # clears all (why 4?)
(row, col, brightness) = (2, 0, 10)
color_matrix.set_pixel(p1, col, row, LEGO_RED, brightness)

led = []
for color in colors:
    led.append((brightness << 4) + color)
color_matrix.set_pixels(p1, bytes(led))

# make sure to convert to list to bytes




