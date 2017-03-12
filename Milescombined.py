from picamera import PiCamera
from time import sleep
from espeak import espeak
from gpiozero import MotionSensor

pir = MotionSensor(4)

camera = PiCamera()


while True:
    if pir.motion_detected:
		camera.rotation = 180
		camera.start_preview()
		sleep(5)
		camera.capture('milespic.jpg')
		camera.stop_preview()
		espeak.synth("I have spotted a thing, it could be a child or Miles the cat")
		sleep(5)
