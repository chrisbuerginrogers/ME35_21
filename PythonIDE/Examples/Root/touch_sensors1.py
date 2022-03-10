#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())

duration = 0.15


@event(robot.when_touched, [True, False, False, False])
async def when_touch_fl(robot):
    await robot.set_lights_rgb(255, 0, 0)  # red
    await robot.play_tone(440, duration)  # A4


@event(robot.when_touched, [False, True, False, False])
async def when_touch_fr(robot):
    await robot.set_lights_rgb(0, 255, 0)  # green
    await robot.play_tone(554, duration)  # C#5


@event(robot.when_touched, [False, False, True, False])
async def when_touch_bl(robot):
    await robot.set_lights_rgb(0, 0, 255)  # blue
    await robot.play_tone(659, duration)  # E5


@event(robot.when_touched, [False, False, False, True])
async def when_touch_br(robot):
    await robot.set_lights_rgb(255, 255, 255)  # white
    await robot.play_tone(880, duration)  # A5


@event(robot.when_play)
async def when_play(robot):
    await robot.say("Hello!")

robot.play()
