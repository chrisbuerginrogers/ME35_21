#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())

speed = 10.0


@event(robot.when_touched, [True, False, False, False])
async def when_touched(robot):
    print('0')


@event(robot.when_touched, [False, True, False, False])
async def when_touched(robot):
    print('1')


@event(robot.when_touched, [False, False, True, False])
async def when_touched(robot):
    print('2')


@event(robot.when_touched, [False, False, False, True])
async def when_touched(robot):
    print('3')


@event(robot.when_touched, [])
async def when_touched(robot):
    print('ANY')


robot.play()
