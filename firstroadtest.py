from adafruit_motorkit import MotorKit
kit = MotorKit()
import time

# Forward at full throttle
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
# A 1.0 second sleep pauses the code while
# motors are running. After 1.0 sec., the
# lines after sleep will set throttle to zero,
# effectively turning the motor off.
time.sleep(1.0)
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(1.0)

# back at half throttle
kit.motor1.throttle = -0.5
kit.motor2.throttle = -0.5
# A 1.0 second sleep pauses the code while
# motors are running. After 1.0 sec., the
# lines after sleep will set throttle to zero,
# effectively turning the motor off.
time.sleep(1.0)
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(1.0)

# right at full throttle
kit.motor1.throttle = 1.0
kit.motor2.throttle = -1.0
# A 1.0 second sleep pauses the code while
# motors are running. After 1.0 sec., the
# lines after sleep will set throttle to zero,
# effectively turning the motor off.
time.sleep(1.0)
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(1.0)

# left at full throttle
kit.motor1.throttle = -1.0
kit.motor2.throttle = 1.0
# A 1.0 second sleep pauses the code while
# motors are running. After 1.0 sec., the
# lines after sleep will set throttle to zero,
# effectively turning the motor off.
time.sleep(1.0)
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(1.0)
