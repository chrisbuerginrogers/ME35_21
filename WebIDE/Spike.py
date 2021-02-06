# Builds the McGinn Page for Spike
import RogersSerial
RogersSerial.processor = 'SPIKE'

RogersSerial.pyCode = \
    {'simple':
         {'Beep':['Make your SPIKE beep','''import hub\nhub.sound.beep()'''],
          'Lights':['Change the color of the light','''import hub\nhub.led(3) # blue   (colors 0 - 10)'''],
          'Display':['Display a face','''import hub\nhub.display.show(hub.Image.HAPPY)'''],
          'Motor':['Turn on a motor',
                   '''import hub, utime\nhub.port.A.motor.pwm(100)\nutime.sleep(1)\nhub.port.A.motor.float()'''],
          'Motors':['Turn on a pair of motors',
                    '''import hub \n# only works if both motors are connected \nmotor = hub.port.A.motor.pair(hub.port.B.motor)\nmotor.pwm(40,-40) # drive straight\nmotor.run_for_time(200,40,-40)''']
          },
    'accel':
          {'ReadAccel':['Read Acclerometer','''import hub\nhub.motion.accelerometer()'''],
           'Monitor':['Monitor Acceleration',
                        '''while not hub.button.center.is_pressed():
                                 gravity = hub.motion.accelerometer()
                                 Xgravity = gravity [0] /100
                                 Ygravity = gravity [1] /100
                                 Zgravity = gravity[2] /100
                                 print('%g, %g, %g' % (Xgravity,Ygravity,Zgravity))
                                 freq = int(-Xgravity *100)
                                 hub.sound.beep(freq, 10, 1)
                                 utime.sleep_ms(9)'''],
          }
      }


from http.server import HTTPServer
import webbrowser

# Set host port
host_port = 8000
ip_address = 'localhost'


# Create Webserver
if __name__ == '__main__':

    http_server = HTTPServer((ip_address, host_port), RogersSerial.MyServer)
    print("Server Starts - %s:%s" % (ip_address, host_port))
    webbrowser.open_new('http://%s:%s' %  (ip_address, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        print("\n-------------------EXIT-------------------")
