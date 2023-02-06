'''
SmartMotor

Run this program then move the motor and cover 
the light sensor and hit the right button for each training point.
When you are done, hit the center button - the motor should
move to the closest training point.  Hit the center button
again to stop.
'''

import hub, utime, port
import color_sensor, display, sound, motor, button

ledBright = 100
motorSpeed = 5000

class SmartPlot():
    def __init__(self, motorPort, lightPort):
        self.motorPort = motorPort
        self.angle = lambda : port.port_getSensor(motorPort)[2]
        self.light = lambda :color_sensor.get_reflection(lightPort)
        self.beep = sound.beepPlay
#        self.led = hub.led
        self.clearscreen = display.display_clear
        self.pixel = display.display_set_pixel
        self.save = lambda : button.button_pressed(button.BUTTON_RIGHT)
        self.done = lambda : button.button_pressed(button.BUTTON_ON_OFF)
        self.quit = lambda : button.button_pressed(button.BUTTON_LEFT)
        self.training = []

    def Setup(self):
        self.beep()
        self.clearscreen()
        return
            
    def Map(self,x=-1,y=-1,bar = True):
        X,Y=0,0
        self.clearscreen()
        for (a,l) in self.training:
            Y = round(l /100 * 4)
            X = round((a + 180) / 360 * 4)
            X = 5-X if X < 0 else X
            if bar:
                for i in range(5):
                    self.pixel(i,Y,50)
                    self.pixel(X,i,50)
            self.pixel(X,Y,ledBright)
        if (x<0):
            return
        Y = round(x /100 * 4)
        X = round((y + 180) / 360 * 4)
        X = 5-X if X < 0 else X
        self.pixel(X,Y, int(0.9*ledBright))

    def Train(self):
#        self.led(3)
        motor.motor_move_to_position(self.motorPort, 0, motorSpeed, motor.MOTOR_END_STATE_COAST)
        utime.sleep(.1)
        self.Map()   
        while not self.done():
            while not self.save() and not self.done(): 
                if self.quit():   #did they want to quit?
                    return 
                utime.sleep(.1) # debounce 
                self.Map(self.light(),self.angle())
            if not self.done():
                angle = self.angle()
                print(angle)
                bright = self.light()
                while self.save():
                    utime.sleep(.1)
                self.training.append((angle,bright))
                print('(%d,%d)'%(angle,bright))
        while self.done(): 
            utime.sleep(.1) # debounce        
        self.beep()
#        self.led(0)
        self.clearscreen()
        
    def Run(self):
#        self.led(2)
        self.Map()   
        # grab reading
        while not self.done():
            if self.quit():
                return  #did they want to quit?
            bright = self.light()
            min = 1000
            pos = 0
            for (a, l) in self.training:
                dist = abs(bright - l)
                if dist < min:
                    min = dist
                    pos = a
            self.Map(bright,pos)
            motor.motor_move_to_position(self.motorPort, pos, motorSpeed, motor.MOTOR_END_STATE_HOLD)
            utime.sleep(.1)
            #print('(%d,%d)'%(pos,bright)) 
        while self.done(): 
            utime.sleep(.1) # debounce     
        self.beep()
#        self.led(0)
        self.clearscreen()

SP = SmartPlot(port.PORTE,port.PORTC)

SP.Setup()
while not SP.quit():
    SP.Train()
    SP.Run()
SP.beep()
#SP.led(10)
SP.clearscreen()
motor.motor_stop(SP.motorPort)

# hub.power_off()
