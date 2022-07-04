import button
import time

fred = button.button_isPressed(button.BUTTON_RIGHT)
if fred[0]:   # fred is (0 or 1,time)
    print('pressed for %d msec'% (fred[1]))

if fred > (1,2000):
    print('let go of the button')
    
btn = {
    0:'power',
    1:'left',
    2:'right',
    3:'connect',
   }

while True:
    for press in btn:
        if button.button_isPressed(press)[0]:
            print('The %s button is pressed' % btn[press])
    time.sleep(0.1)
    