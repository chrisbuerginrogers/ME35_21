#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())


@event(robot.when_play)
async def draw_square(robot):
    await robot.set_marker(Root.MARKER_DOWN)
    for _ in range(4):
        await robot.move(6)  # cm
        await robot.turn_left(90)  # deg
    await robot.set_marker(Root.MARKER_UP)

robot.play()
