from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
blue = [([86, 31, 4], [220, 88, 50])]
red = [([17, 15, 100], [50, 56, 200])]
yellow = [([5, 130, 155], [62, 174, 250])]
green = [([25, 109, 0], [83, 250, 106])]
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cube = image[250:300, 200:250]
    # blue
    for (lower, upper) in blue:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(cube, lower, upper)
    b = sum(sum(mask))
    print
    "blue"
    print
    b
    # red
    for (lower, upper) in red:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(cube, lower, upper)
    r = sum(sum(mask))
    print
    "red"
    print
    r
    # green
    for (lower, upper) in green:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(cube, lower, upper)
    g = sum(sum(mask))
    print
    "green"
    print
    g
    # yellow
    for (lower, upper) in yellow:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(cube, lower, upper)
    y = sum(sum(mask))
    print
    "yellow"
    print
    y
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    if b < 1000 and r < 1000 and y < 1000 and g < 1000:
        print
        "no block"
    else:
        if b > r and b > g and b > y:
            print
            "block blue"
        elif r > g and r > y:
            print
            "block red"
            # blinking function

            GPIO.output(11, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(11, GPIO.LOW)

        elif y > g:
            print
            "block yellow"

            GPIO.output(7, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(7, GPIO.LOW)

        else:
            print
            "block green"

            GPIO.output(13, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(13, GPIO.LOW)

    GPIO.cleanup()
    cv2.imshow("cube", cube)

    print
    cube[30][30]
    cv2.rectangle(image, (200, 250), (250, 300), (0, 0, 255), 2)
    cv2.imshow("original", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break