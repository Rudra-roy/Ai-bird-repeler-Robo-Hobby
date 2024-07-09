import RPi.GPIO as GPIO
import time

# Define GPIO pins for ULN2003 driver
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Set the number of steps per revolution for 28BYJ-48
steps_per_revolution = 1024

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Define the step sequence for 28BYJ-48
step_sequence = [
    [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
    [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
    [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
    [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
    [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
    [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
    [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
]

# Function to perform one step
def step_motor(step):
    for pin in range(4):
        GPIO.output([IN1, IN2, IN3, IN4][pin], step_sequence[step][pin])
    time.sleep(0.01)  # Adjust delay for motor speed

# Function to rotate the motor a given number of steps
def rotate_motor(steps):
    for _ in range(steps):
        for step in range(8):
            step_motor(step)

# Function to rotate the motor in reverse a given number of steps
def rotate_motor_reverse(steps):
    for _ in range(steps):
        for step in reversed(range(8)):
            step_motor(step)

try:
    while True:
        # Rotate 180 degrees clockwise (half a revolution)
        rotate_motor(steps_per_revolution // 2)
        time.sleep(1)  # Wait for 1 second
        
        # Rotate 180 degrees counterclockwise (half a revolution)
        rotate_motor_reverse(steps_per_revolution // 2)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Cleanup GPIO settings
    GPIO.cleanup()
