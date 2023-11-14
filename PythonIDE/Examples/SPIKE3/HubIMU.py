from hub import motion_sensor
import time

faces = {
    0:'HUB_FACE_TOP',
    1:'HUB_FACE_FRONT',
    2:'HUB_FACE_RIGHT',
    3:'HUB_FACE_BOTTOM',
    4:'HUB_FACE_BACK',
    5:'HUB_FACE_LEFT',
    }
    
gestures = [
    motion_sensor.TAPPED,
    motion_sensor.DOUBLE_TAPPED,
    motion_sensor.SHAKEN,
    motion_sensor.FALLING,
    motion_sensor.UNKNOWN,
    ]
    
Yaw_Face = [
    motion_sensor.TOP,    # The SPIKE Prime hub face with the USB charging port.
    motion_sensor.FRONT,  # The SPIKE Prime hub face with the Light Matrix.
    motion_sensor.RIGHT,  # The right side of the SPIKE Prime hub when facing the front hub face.
    motion_sensor.BOTTOM, # The side of the SPIKE Prime hub where the battery is.
    motion_sensor.BACK,   # The SPIKE Prime hub face where the speaker is.
    motion_sensor.LEFT,   # The left side of the SPIKE Prime hub when facing the front hub face.
    ]

motion_sensor.get_yaw_face()
motion_sensor.stable()  # True means not moving
motion_sensor.gesture()
motion_sensor.tilt_angles() # yaw pitch and roll values as integers. Values are decidegrees
faces[motion_sensor.up_face()]
motion_sensor.quaternion()
motion_sensor.acceleration() #The values are mili G, so 1 / 1000 G
motion_sensor.angular_velocity() # The values are decidegrees per second

motion_sensor.reset_tap_count()
print('tap it')
time.sleep(5)
print(motion_sensor.tap_count())
