#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())


async def fractal(level, size):
    if level < 1:
        await robot.move(size)
    else:
        await fractal(level - 1, size/3)
        await robot.turn_left(60)
        await fractal(level - 1, size/3)
        await robot.turn_left(-120)
        await fractal(level - 1, size/3)
        await robot.turn_left(60)
        await fractal(level - 1, size/3)


@event(robot.when_play)
async def when_play(robot):
    await robot.set_lights(Root.LIGHT_SPIN, Color(0, 0, 255))
    await robot.set_marker(Root.MARKER_DOWN)

    for _ in range(3):
        await fractal(3, 40)
        await robot.turn_left(-120)

    await robot.set_marker(Root.MARKER_UP)

robot.play()
