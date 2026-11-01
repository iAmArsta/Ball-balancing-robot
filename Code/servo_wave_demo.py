import math
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
servos = [kit.servo[0], kit.servo[1], kit.servo[2]]

MAX_ANGLE = 60
DELAY = 0.005


for servo in servos:
    servo.angle = 0

time.sleep(5)

try:
    while True:
        for angle in list(range(MAX_ANGLE + 1)) + list(range(MAX_ANGLE, -1, -1)):
            for servo in servos:
                servo.angle = angle
            time.sleep(DELAY)

        steps_per_cycle = 100
        total_steps = 4 * steps_per_cycle
        for step in range(total_steps + 1):
            phase = 2 * math.pi * step / steps_per_cycle
            fade = min(1.0, step / 50, (total_steps - step) / 50)
            for i, servo in enumerate(servos):
                angle = fade * MAX_ANGLE / 2 * (1 + math.sin(phase + i * 2 * math.pi / 3))
                servo.angle = angle
            time.sleep(DELAY)

except KeyboardInterrupt:
    print("Stopped")
