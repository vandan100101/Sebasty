# import RPi.GPIO as GPIO

# left_motor_pin1 = 17
# left_motor_pin2 = 18
# right_motor_pin1 = 22
# right_motor_pin2 = 23

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(left_motor_pin1, GPIO.OUT)
# GPIO.setup(left_motor_pin2, GPIO.OUT)
# GPIO.setup(right_motor_pin1, GPIO.OUT)
# GPIO.setup(right_motor_pin2, GPIO.OUT)

# def move_forward():
#     GPIO.output(left_motor_pin1, GPIO.HIGH)
#     GPIO.output(left_motor_pin2, GPIO.LOW)
#     GPIO.output(right_motor_pin1, GPIO.HIGH)
#     GPIO.output(right_motor_pin2, GPIO.LOW)

# def move_backward():
#     GPIO.output(left_motor_pin1, GPIO.LOW)
#     GPIO.output(left_motor_pin2, GPIO.HIGH)
#     GPIO.output(right_motor_pin1, GPIO.LOW)
#     GPIO.output(right_motor_pin2, GPIO.HIGH)

# def turn_left():
#     GPIO.output(left_motor_pin1, GPIO.LOW)
#     GPIO.output(left_motor_pin2, GPIO.HIGH)
#     GPIO.output(right_motor_pin1, GPIO.HIGH)
#     GPIO.output(right_motor_pin2, GPIO.LOW)

# def turn_right():
#     GPIO.output(left_motor_pin1, GPIO.HIGH)
#     GPIO.output(left_motor_pin2, GPIO.LOW)
#     GPIO.output(right_motor_pin1, GPIO.LOW)
#     GPIO.output(right_motor_pin2, GPIO.HIGH)

# def stop_robot():
#     GPIO.output(left_motor_pin1, GPIO.LOW)
#     GPIO.output(left_motor_pin2, GPIO.LOW)
#     GPIO.output(right_motor_pin1, GPIO.LOW)
#     GPIO.output(right_motor_pin2, GPIO.LOW)
