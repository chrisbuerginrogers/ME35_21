import color_sensor
import port

light = port.PORTA

# Get color - see Defines.py for the list of colors
colors = {
    -1:'ERR',
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

colors[color_sensor.get_color(light)]
color_sensor.get_reflection(light)
color_sensor.get_rgbi(light)  #RGBI
