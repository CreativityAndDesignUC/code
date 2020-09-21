from gpiozero import MotionSensor

pir = MotionSensor('GPIO26')
print("waiting")
pir.wait_for_motion()
print("Motion detected!")
