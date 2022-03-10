#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())


@event(robot.when_play)
async def when_play(robot):
    await robot.set_wheel_speeds(10, 10)  # cm/s


@event(robot.when_color_scanned, [])
async def when_color_scanned(robot):
    colors = robot.color_sensor.colors
    sum, num = 0, 0
    half = (len(colors) - 1) / 2
    for i, color in enumerate(colors):
        if color != Color.WHITE:
            sum += i
            num += 1
    pos = (sum / num - half) / half if num else 0
    await robot.set_wheel_speeds((pos + 0.5) * 20, (0.5 - pos) * 20)

robot.play()
