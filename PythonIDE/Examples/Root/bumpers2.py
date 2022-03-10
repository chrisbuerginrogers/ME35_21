#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())

speed = 10.0


@event(robot.when_bumped, [True, False])
async def when_bumper(robot):
    await robot.set_lights_rgb(255, 0, 0)  # red
    await robot.set_wheel_speeds(-speed, speed)
# Alternative syntax (the @event decorator must be commented out)
# robot.when_bumped([True, False], when_bumper)


@event(robot.when_bumped, [False, True])
async def when_bumper(robot):
    await robot.set_lights_rgb(0, 255, 0)  # green
    await robot.set_wheel_speeds(speed, -speed)


@event(robot.when_bumped, [])
async def when_bumped(robot):
    while True:
        await robot.play_tone(440, .1)
        await robot.wait(0.3)
        await robot.play_tone(880, .1)
        await robot.wait(0.3)


@event(robot.when_play)
async def when_play(robot):
    print('Hello!')
    await robot.turn_left(90)
    print("Bye!")


@event(robot.when_play)
async def when_play(robot):
    print("Bye!")

robot.play()
