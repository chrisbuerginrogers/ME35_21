import motor, port

(p1,p2) = (port.PORTD, port.PORTF)

position = port.port_getSensor(p2)[1]
speed = port.port_getSensor(p2)[0]
angle = port.port_getSensor(p2)[2]

motor.motor_move_by_degrees(p1, 180, 2000)
motor.motor_move_by_degrees(p2, 180, 2000)

power = 1000
speed = 1000
motor.motor_move_at_power(p1, power)
motor.motor_move_at_speed(p1, speed)
duration = 1000
motor.motor_move_for_time(p1, duration, speed,motor.MOTOR_END_STATE_BRAKE)
degrees = 360
motor.motor_move_by_degrees(p1, speed, degrees, motor.MOTOR_END_STATE_HOLD)
motor.motor_move_to_position(p1, speed, degrees,motor.MOTOR_END_STATE_FLOAT)
motor.motor_move_to_absolute_position(p1, speed, degrees,
            motor.MOTOR_MOVE_DIRECTION_CCW,
            motor.MOTOR_END_STATE_HOLD)

motor.motor_stop(p1)

motor.motor_move_for_time((p1, p2), speed, duration)
motor.motor_move_for_time((p1, p2), (1000, 4000),
        (5000, 2000),motor.MOTOR_END_STATE_FLOAT)

#motor.motor_move_for_time(p1, speed, duration,
#                        endstate = motor.MOTOR_END_STATE_BRAKE,
#                        defer= True )

import util

async def main():
    await motor.motor_move_by_degrees(p1, 180, 2000,motor.MOTOR_END_STATE_FLOAT)
    motor.motor_move_by_degrees(p2, 180, 2000,motor.MOTOR_END_STATE_FLOAT)

util.run(main())
