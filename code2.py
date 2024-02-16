## ---- Imports ---- ##
from piper_blockly import *
import board
import time
from digitalio import Pull

## ---- Definitions ---- ##

GP0 = piperServoPin(board.GP0, "GP0")

try:
  set_digital_view(True)
except:
  pass

GP2 = piperPin(board.GP2, "GP2")
GP1 = piperServoPin(board.GP1, "GP1")

# Define a variable to track the number of feedings
num_feedings = 0
max_feedings = 10  # Define the maximum number of feedings before considering the robot full

# Function to perform feeding action
def feed_robot():
    global num_feedings
    if num_feedings < max_feedings:
        playSound("drumkit-Clap1")
        print('High')
        GP1.setServoAngle(0)
        time.sleep(1)
        GP1.setServoAngle(180)
        time.sleep(0.6)
        num_feedings += 1
    else:
        print("Robot is full, cannot eat anymore.")

# Main loop
playSound("electro-NightRoll-A")
GP0.setServoFraction(min(max(50 * 0.0018 + 0.5, 0), 1))
while True:
    if GP2.checkPin(None):
        feed_robot()
    time.sleep(0.5)
