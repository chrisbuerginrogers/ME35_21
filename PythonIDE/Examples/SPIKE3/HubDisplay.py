import time

from hub import light_matrix
from hub import light
import color

# Change the power button light to red (light.CONNECT gives the BLE btn)
light.color(light.POWER, color.RED)

light_matrix.clear()
light_matrix.write("LEGO")

row,col,bright = 1,2,100
light_matrix.set_pixel(col,row,bright)
print(light_matrix.get_pixel(row,col))

images = [light_matrix.CANCELLED,
            light_matrix.IMAGE_ANGRY,
            light_matrix.IMAGE_ARROW_E,
            light_matrix.IMAGE_ARROW_N,
            light_matrix.IMAGE_ARROW_NE,
            light_matrix.IMAGE_ARROW_NW,
            light_matrix.IMAGE_ARROW_S,
            light_matrix.IMAGE_ARROW_SE,
            light_matrix.IMAGE_ARROW_SW,
            light_matrix.IMAGE_ARROW_W,
            light_matrix.IMAGE_ASLEEP,
            light_matrix.IMAGE_BUTTERFLY,
            light_matrix.IMAGE_CHESSBOARD,
            light_matrix.IMAGE_CLOCK1,
            light_matrix.IMAGE_CLOCK2,
            light_matrix.IMAGE_CLOCK3,
            light_matrix.IMAGE_CLOCK4,
            light_matrix.IMAGE_CLOCK5,
            light_matrix.IMAGE_CLOCK6,
            light_matrix.IMAGE_CLOCK7,
            light_matrix.IMAGE_CLOCK8,
            light_matrix.IMAGE_CLOCK9,
            light_matrix.IMAGE_CLOCK10,
            light_matrix.IMAGE_CLOCK11,
            light_matrix.IMAGE_CLOCK12,
            light_matrix.IMAGE_CONFUSED,
            light_matrix.IMAGE_COW,
            light_matrix.IMAGE_DIAMOND,
            light_matrix.IMAGE_DIAMOND_SMALL,
            light_matrix.IMAGE_DUCK,
            light_matrix.IMAGE_FABULOUS,
            light_matrix.IMAGE_GHOST,
            light_matrix.IMAGE_GIRAFFE,
            light_matrix.IMAGE_GO_DOWN,
            light_matrix.IMAGE_GO_LEFT,
            light_matrix.IMAGE_GO_RIGHT,
            light_matrix.IMAGE_GO_UP,
            light_matrix.IMAGE_HAPPY,
            light_matrix.IMAGE_HEART,
            light_matrix.IMAGE_HEART_SMALL,
            light_matrix.IMAGE_HOUSE,
            light_matrix.IMAGE_MEH,
            light_matrix.IMAGE_MUSIC_CROTCHET,
            light_matrix.IMAGE_MUSIC_QUAVER,
            light_matrix.IMAGE_MUSIC_QUAVERS,
            light_matrix.IMAGE_NO,
            light_matrix.IMAGE_PACMAN,
            light_matrix.IMAGE_PITCHFORK,
            light_matrix.IMAGE_RABBIT,
            light_matrix.IMAGE_ROLLERSKATE,
            light_matrix.IMAGE_SAD,
            light_matrix.IMAGE_SILLY,
            light_matrix.IMAGE_SKULL,
            light_matrix.IMAGE_SMILE,
            light_matrix.IMAGE_SNAKE,
            light_matrix.IMAGE_SQUARE,
            light_matrix.IMAGE_SQUARE_SMALL,
            light_matrix.IMAGE_STICKFIGURE,
            light_matrix.IMAGE_SURPRISED,
            light_matrix.IMAGE_SWORD,
            light_matrix.IMAGE_TARGET,
            light_matrix.IMAGE_TORTOISE,
            light_matrix.IMAGE_TRIANGLE,
            light_matrix.IMAGE_TRIANGLE_LEFT,
            light_matrix.IMAGE_TSHIRT,
            light_matrix.IMAGE_UMBRELLA,
            light_matrix.IMAGE_XMAS,
            light_matrix.IMAGE_YES]
            
for i,image in enumerate(images):
    print(i, image)
    light_matrix.show_image(image)
    time.sleep(0.1)     
    
orientation={'up': 0, 'left': 1, 'down':2, 'right': 3}
    
for o in orientation:
    print(orientation[o])
    light_matrix.set_orientation(orientation[o])
    time.sleep(1)

if not (light_matrix.get_orientation() == orientation['up']): 
    light_matrix.set_orientation(orientation['up'])
    
         