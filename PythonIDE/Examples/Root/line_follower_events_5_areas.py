#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())

speed = 6.0
half_speed = 0.5*speed


@event(robot.when_color_scanned, [Color.GREEN, Color.ANY, Color.ANY, Color.ANY, Color.ANY])
async def left_full(robot):
    await robot.set_wheel_speeds(0, speed)


@event(robot.when_color_scanned, [Color.GREEN, Color.ANY, Color.ANY, Color.ANY, Color.ANY])
async def left_half(robot):
    await robot.set_wheel_speeds(half_speed, speed)


@event(robot.when_color_scanned, [Color.ANY, Color.ANY, Color.ANY, Color.ANY, Color.GREEN])
async def right_full(robot):
    await robot.set_wheel_speeds(speed, 0)


@event(robot.when_color_scanned, [Color.ANY, Color.ANY, Color.ANY, Color.ANY, Color.GREEN])
async def right_half(robot):
    await robot.set_wheel_speeds(speed, half_speed)


@event(robot.when_color_scanned, [Color.ANY, Color.ANY, Color.GREEN, Color.ANY, Color.ANY])
async def forward(robot):
    await robot.set_wheel_speeds(speed, speed)


@event(robot.when_play)
async def when_play(robot):
    await robot.say("Following!")
    await robot.set_lights(Root.LIGHT_SPIN, Color(0, 0, 255))
    await robot.set_wheel_speeds(speed, speed)

robot.play()
