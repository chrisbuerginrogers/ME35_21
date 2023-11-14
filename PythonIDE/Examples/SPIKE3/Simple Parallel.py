import runloop
import motor
from hub import port
import display

p1,p2 = port.E,port.F

async def motor_stack():
    degrees = 180
    speed = 1000
    await motor.motor_move_by_degrees(p1, degrees, speed)
    await motor.motor_move_by_degrees(p2, degrees, speed,motor.MOTOR_END_STATE_FLOAT)
    await motor.motor_move_by_degrees(p1, -1 * degrees, speed,motor.MOTOR_END_STATE_FLOAT)
    
async def hub_pixel_stack():
    display.display_set_pixel(1,1, 100)
    await util.wait_for_time(2000)
    display.display_clear()
    await util.wait_for_time(1000)
    display.display_set_pixel(2,2, 100)
    
util.run(motor_stack(), hub_pixel_stack())
