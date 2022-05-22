#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())

speed = 10.0


@event(robot.when_bumped, [True, False])
async def when_bumper(robot):
    print('LEFT')
    await robot.turn_left(90)


@event(robot.when_bumped, [False, True])
async def when_bumper(robot):
    print('RIGHT')
    await robot.turn_right(90)

@event(robot.when_bumped, [])
async def when_bumped(robot):
    print('ANY')

robot.play()
