#
# Licensed under 3-Clause BSD license available in the License file. Copyright (c) 2021 iRobot Corporation. All rights reserved.
#

from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3

robot = Root(Bluetooth())

speed = 6  # cm/s
color_to_detect = Color.GREEN


@event(robot.when_play)
async def when_play(robot):
    await robot.set_wheel_speeds(speed, speed)

    while True:
        # slices the colors getter in 5 areas
        colors_left0 = robot.color_sensor.colors[0:6]
        colors_left1 = robot.color_sensor.colors[6:12]
        colors_center = robot.color_sensor.colors[12:20]
        colors_right1 = robot.color_sensor.colors[20:26]
        colors_right0 = robot.color_sensor.colors[26:32]

        if color_to_detect in colors_left0:
            robot.set_wheel_speeds(0, speed)
        elif color_to_detect in colors_right0:
            robot.set_wheel_speeds(speed, 0)
        elif color_to_detect in colors_left1:
            robot.set_wheel_speeds(0.5*speed, speed)
        elif color_to_detect in colors_right1:
            robot.set_wheel_speeds(speed, 0.5*speed)
        elif color_to_detect in colors_center:
            robot.set_wheel_speeds(speed, speed)

robot.play()
