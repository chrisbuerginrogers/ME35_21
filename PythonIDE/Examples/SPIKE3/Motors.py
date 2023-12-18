from hub import port
import motor
import time

motors =[port.E, port.F]

'''
Small motor (essential): -660 to 660
Medium motor: -1110 to 1110
Large motor: -1050 to 1050
'''
speed = 500
for m in motors: 
    motor.run(m, speed)
time.sleep(1)
for m in motors: 
    motor.stop(m)

motor.absolute_position(port.E) # -180 to 180
motor.velocity(port.E)
motor.get_duty_cycle(port.E)
motor.relative_position(port.E) # -infinity to + infinity

motor.reset_relative_position(port.E)
motor.relative_position(port.E)

for i in range(10):
    print(motor.absolute_position(port.E))
    time.sleep(1)

#  --------- moving the motors
pwm = 5000  # from -10,000 to 10,000
motor.set_duty_cycle(port.E,pwm)
time.sleep(1)
motor.set_duty_cycle(port.E,0)

motor.run_for_degrees(port.E,20,100)

motor.run_for_degrees(port.E, 
                20,                   # degrees
                100,                  # degrees/sec
                stop = motor.BRAKE,   # see below
                acceleration = 1000,  # (deg/sec) (0 - 10000)
                deceleration = 1000)  # (deg/sec) (0 - 10000)
    
motor.run_for_time(port.E, 
                2000,                 # milliseconds
                100,                  # degrees/sec
                stop = motor.BRAKE,   # see below
                acceleration = 1000,  # (deg/sec) (0 - 10000)
                deceleration = 1000)  # (deg/sec) (0 - 10000)

motor.run_to_absolute_position(port.E, 
                20,                   # degrees (-180 to 180)
                100,                  # degrees/sec
                direction = motor.SHORTEST_PATH,   # motor.CLOCKWISE motor.COUNTERCLOCKWISE, motor.SHORTEST_PATH, motor.LONGEST_PATH
                stop = motor.BRAKE,   # see below
                acceleration = 1000,  # (deg/sec) (0 - 10000)
                deceleration = 1000)  # (deg/sec) (0 - 10000)
    
motor.run_to_relative_position(port.E, 
                20,                   # degrees (-infinity to infinity)
                100,                  # degrees/sec
                stop = motor.BRAKE,   # see below
                acceleration = 1000,  # (deg/sec) (0 - 10000)
                deceleration = 1000)  # (deg/sec) (0 - 10000)
    

'''
STOP modes:
motor.COAST to make the motor coast until a stop
motor.BREAK to brake and continue to brake after stop
motor.HOLD to tell the motor to hold it's position
motor.CONTINUE to tell the motor to keep running at whatever velocity it's running at until it gets another command
motor.SMART_COAST to make the motor brake until stop and then coast and compensate for inaccuracies in the next command
motor.SMART_BRAKE to make the motor brake and continue to brake after stop and compensate for inaccuracies in the next command                

Awaitable status
motor.READY
motor.RUNNING
motor.STALLED
motor.CANCELED
motor.ERROR
motor.DISCONNECTED
'''

import runloop

async def main():
    await motor.run_for_degrees(port.E, 180, 200, stop = motor.HOLD)
    await runloop.sleep_ms(2000)
    await motor.run_for_degrees(port.E, 0, 200, stop = motor.COAST)
    print('done')
runloop.run(main())

#--------------------- Motor pairing

import motor_pair

motor_pair.unpair(motor_pair.PAIR_1)   # remove any old pairing
motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

motor_pair.move(motor_pair.PAIR_1, 
                    0,                      # steering (-100 to 100)
                    velocity=280,           # speed 
                    acceleration=100)
time.sleep(2)                   
motor_pair.stop(motor_pair.PAIR_1)

motor_pair.move_for_degrees(motor_pair.PAIR_1, 
                            500,             # relative
                            0,               # steering (-100 to 100)
                            velocity=280, 
                            deceleration=10)
                            
motor_pair.move_for_time(motor_pair.PAIR_1, 
                        1000,                  # time in millisec
                        0,                     # steering (-100 to 100)
                        velocity=280, 
                        deceleration=10)

motor_pair.move_tank(motor_pair.PAIR_1, 
                        1000,                # left speed (deg/sec)
                        -1000)               # right speed (deg/sec)
                        
motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 
                        720,                 # degrees (relative)
                        1000,                # left speed (deg/sec)
                        -1000)               # right speed (deg/sec)

motor_pair.move_tank_for_time(motor_pair.PAIR_1, 
                        1000,                # time (millisec)
                        -1000,                # left speed (deg/sec)
                        2000)               # right speed (deg/sec)
                        
import runloop

async def main():
    motor_pair.move(motor_pair.PAIR_1,10)  
    await runloop.sleep_ms(2000)
    motor_pair.move_tank(motor_pair.PAIR_1, 1000, -1000)   
    await runloop.sleep_ms(2000)
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, -1000, 2000)
    print('done')
    
runloop.run(main())
