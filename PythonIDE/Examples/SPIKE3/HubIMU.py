import imu

faces = {
    0:'HUB_FACE_TOP',
    1:'HUB_FACE_FRONT',
    2:'HUB_FACE_RIGHT',
    3:'HUB_FACE_BOTTOM',
    4:'HUB_FACE_BACK',
    5:'HUB_FACE_LEFT',
    }

imu.getTemperature()
imu.getGesture()
imu.getGyro()
faces[imu.getUpFace()]
imu.getQuaternion()
imu.getOrientation()
imu.getAcceleration()
#imu.setImpact()
#setOrientationYawFace()
#setYawValue()
