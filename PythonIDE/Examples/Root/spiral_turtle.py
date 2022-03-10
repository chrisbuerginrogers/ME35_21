#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

# Turtle geometry simple spiral.

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3


robot = Root(Bluetooth())


@event(robot.when_play)
async def spiral(robot):
    await robot.set_marker(Root.MARKER_DOWN)
    for i in range(0, 40):
        await robot.turn_left(2*i + 10)
        await robot.move(5)
    await robot.set_marker(Root.MARKER_UP)

robot.play()
