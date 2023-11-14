from hub import button
import time

fred = button.pressed(button.LEFT)
if fred:   
    print('pressed for %d msec'% (fred))

if fred > 2000:
    print('let go of the button')
    
btn = {
    0:'power',
    1:'left',
    2:'right',
    3:'connect',
   }

while True:
    for press in btn:
        if button.pressed(press):
            print('The %s button is pressed' % btn[press])
    time.sleep(0.1)


while not button.pressed(button.LEFT): # Wait for the left button to be pressed 
    pass

# As long as the left button is being pressed, update the `left_button_press_duration` variable 
while button.pressed(button.LEFT):
    duration = button.pressed(button.LEFT)

print("Left button was pressed for " + str(duration) + " milliseconds")