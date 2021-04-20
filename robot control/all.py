import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


h = ServoKit(channels=16)

direction = [1, 2, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1]
init = [0,90,20,0,180,160,170,180,60,0,0,150]
limit = [35,180,180,0,0,40,0,0,180,180,180,30]

cur = init

def changeDeg(pin1,new1,pin2,new2):
    now1 = cur[pin1]
    now2 = cur[pin2]
    for deg in range(0,max(abs(now1-new1),abs(now2-new2)),5):
        if now1<new1:
            now1=now1+5
        elif now1>new1:
            now1=now1-5
        if now2<new2:
            now2=now2+5
        elif now2>new2:
            now2=now2-5
        h.servo[pin1].angle=now1
        h.servo[pin2].angle=now2
        time.sleep(0.05)
    cur[pin1]=now1
    cur[pin2]=now2
    
    
for i in range(0,12):
    h.servo[i].angle = init[i]
    time.sleep(0.5)
    
#code write here
    
for i in range(0,12):
    h.servo[i].angle = init[i]
    time.sleep(0.5)

