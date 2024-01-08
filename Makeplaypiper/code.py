## ---- Imports ---- ##
from piper_blockly import *
import board
import time
from digitalio import Pull

## ---- Definitions ---- ##

GP1 = piperServoPin(board.GP1, "GP1")

try:
  set_digital_view(True)
except:
  pass

GP4 = piperPin(board.GP4, "GP4")


## ---- Code ---- ##
playSound("winloose-go1")
GP1.setServoAngle(180)
time.sleep(1)
while True:
  GP1.setServoAngle(180)
  time.sleep(1)
  if GP4.checkPin(None):
    print('high')
    playSound("japanese_drum-hirado-A1")
    GP1.setServoAngle(0)
    time.sleep(0.5)

  time.sleep(0.002)
