#Breakout Board Motor Controller
from microbit import *
motorA_FWD = pin8
motorA_REV = pin12
motorB_FWD = pin0
motorB_REV = pin16
while True:
    motorA_REV.write_digital(1)
    motorB_REV.write_digital(1)
    sleep(1000)
    motorA_REV.write_digital(0)
    motorB_REV.write_digital(0)
    sleep(1000)
    motorA_FWD.write_digital(1)
    motorB_FWD.write_digital(1)
    sleep(1000)
    motorA_FWD.write_digital(0)
    motorB_FWD.write_digital(0)