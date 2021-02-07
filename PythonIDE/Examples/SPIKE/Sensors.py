# Force Sensor
​
force_sensor = hub.port.A.device
​
# Get Force Newtons (0-10)
​
force = force_sensor.get()[0]
​
# Get Button Press State (isPressed == 1, notPressed == 0)
​
isPressed = force_sensor.get()[1]
​
​
# Get Force (384-700) (384 - 700)
​
force = force_sensor.get()[2]
​
​
# ----------------------------------------------------------------------------------
​
# Ultrasonic Sensor
​
sonic_sensor = hub.port.A.device
​
​
# Get Distance in centimeters (cm)
​
sonic_sensor.get()[0]
​
# ---------------------------------------------------------------------------------
​
# Light Sensor
​
light_sensor = hub.port.A.device
​
# Get Ambient Light Intensity (0 - 99)
​
light_sensor.get()[0]
​
# Color Value (0-10)
​
# need to figure out the colors
​
light_sensor.get()[1]
​
# RED Color Intensity (0 - 1024)
​
light_sensor.get()[2]
​
# GREEN Color Intensity (0 - 1024)
​
light_sensor.get()[3]
​
# BLUE Color Intensity (0 - 1024)
​
light_sensor.get()[4]
