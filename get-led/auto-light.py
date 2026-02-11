import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
botton = 6
GPIO.setup(botton, GPIO.IN)
while True:
    GPIO.output(led,not GPIO.input(botton))