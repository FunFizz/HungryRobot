## ---- Imports ---- ##
from piper_blockly import *
import board
import time

## ---- Definitions ---- ##

GP1 = piperServoPin(board.GP1, "GP1")

try:
  set_digital_view(True)
except:
  pass

GP26 = piperPin(board.GP26, "GP26", "Analog")


## ---- Code ---- ##
playSound("winloose-go1")
GP1.setServoAngle(180)
time.sleep(1)
while True:
  GP1.setServoAngle(180)
  time.sleep(1)
  if GP26.readVoltage() > 2:
    playSound("japanese_drum-hirado-A1")
    GP1.setServoAngle(0)
    time.sleep(0.5)

  time.sleep(0.002)
