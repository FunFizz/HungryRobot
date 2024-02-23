## ---- Imports ---- ##
from piper_blockly import *
import board
import time
import digitalio
from pwmio import PWMOut
from pitches import tones

from board import *
from time import *

## ---- Definitions ---- ##
try:
  set_digital_view(True)
except:
  pass

#Set up Input and Outout Pins
GP0 = piperServoPin(board.GP0, "GP0")
GP2 = piperPin(board.GP2, "GP2")
GP1 = piperServoPin(board.GP1, "GP1")

# Configure buzzer
pin = digitalio.DigitalInOut(GP28)
pin.direction = digitalio.Direction.OUTPUT

#Initialize buttons on GP21 and GP20 and GP22
btn1 = digitalio.DigitalInOut(board.GP20)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
 
btn2 = digitalio.DigitalInOut(board.GP21)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(board.GP22)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

# Define a variable to track the number of feedings
num_feedings = 0
max_feedings = 10  # Define the maximum number of feedings before considering the robot full

offset=0

# Function to set up parameters
def setup():
    max_feedings=int(input("Enter Maximum Number of Feedings>> "))
    return max_feedings

def sing():
    
    tempo = 0.2

    melody = (
        'a2','','a2','','a2','b2','','cs3',
        'a3','','d4','d4','','fs4','b4','','fs4','a4','',
        'a4','','b4','a4','','fs4','g4','','fs4','e4','',
        'b3','','e4','e4','','g4','cs5','','cs5','b4','',
        'a4','g4','','g4','','fs4','b3','','cs4','','d4','e4','',

        'a2','','a2','','a2','b2','','cs3',
        'a3','','d4','d4','','fs4','b4','','fs4','a4','',
        'a4','','b4','a4','','fs4','g4','','fs4','e4','',
        'b3','','e4','e4','','g4','cs5','','b4','','a4',
        'g4','','g4','fs4','','e4','cs4','','e4','','d4','',

        'd3','','e3','','fs3','',
        'b4','','b4','','a4','g4','a4','b4','a4','',
        'e4','','fs4','gs4','','e4','a4','',
        'b4','','a4','','e4','','fs4','gs4','','e4','a4','',

        'a2','','a3','','a2','',
        'b4','','a4','','g4','',
        'e4','','cs5','','b4','a4','','b4','a4','','g4','',
        'a4','','b4','fs4','','','e4','d4','',

        'd3','','e3','','fs3','',
        'b4','','a4','','g4','',
        'e4','','cs5','','b4','a4','','b4','a4','','g4','',
        'a4','','b4','fs4','','','e4','d4','',
    )
    rhythm = [
        4,2,4,4,4,4,4,4,
        4,4,4,4,4,4,4,4,4,4,2,
        4,4,4,4,4,4,4,4,4,4,2,
        4,4,4,4,4,4,4,4,4,4,4,
        4,4,2,4,4,4,4,4,4,2,4,2,4,

        4,2,4,4,4,4,4,4,
        4,4,4,4,4,4,4,4,4,4,2,
        4,4,4,4,4,4,4,4,4,4,2,
        4,4,4,4,4,4,4,2,4,4,4,
        4,4,4,4,4,4,4,2,4,2,2,4,

        4,2,4,2,4,2,
        4,2,4,4,4,4,4,4,4,2,
        4,4,4,4,4,4,2,1,
        4,2,4,2,4,4,4,4,4,4,2,4,

        4,2,4,2,4,2,
        4,2,4,2,2,1,
        4,2,4,4,4,4,4,4,4,4,2,2,
        4,4,4,2,2,4,4,2,4,

        4,2,4,2,4,2,
        4,2,4,2,2,1,
        4,2,4,4,4,4,4,4,4,4,2,2,
        4,4,4,2,2,4,4,2,4,
    ]

    for tone, length in zip(melody, rhythm):
        beeper = PWMOut(GP18, variable_frequency=True)
        if tones[tone] != 0:
            beeper.duty_cycle = 2 ** 15
            beeper.frequency = tones[tone]
        sleep(tempo/length)
        beeper.deinit()

    sleep(1)
    
def beep(cycle, frequency):
    beeper = PWMOut(GP18, variable_frequency=True)
    beeper.duty_cycle = cycle
    beeper.frequency = frequency
    sleep(0.4)
    beeper.deinit()
    


# Define a variable to track the number of feedings
def calibrate():
    calFlag='Y'
    print("CALIBRATE THE TRAY")
    while(calFlag=='Y'):
        offset=int(input("Enter offset>> "))
        GP1.setServoAngle(180-offset)
        time.sleep(1)
        print(offset)
        calFlag=input("Do you want to enter another offset (Y or N)>>")
        
# Function to empty robot      
def empty():
        GP1.setServoAngle(0)

# Function to close robot
def close():
        GP1.setServoAngle(180-offset)
        
# Function to perform feeding action
def feed_robot():
    global num_feedings
    if num_feedings < max_feedings:
        playSound("drumkit-Clap1")
        beep(8000,1519)
        print('High')
        GP1.setServoAngle(0)
        sleep(1)
        GP1.setServoAngle(180)
        sleep(0.6)
        num_feedings += 1
    else:
        print("Robot is full, cannot eat anymore.")
        
                          
# Getting ready
playSound("electro-NightRoll-A")
print("End of Sound.")
GP0.setServoFraction(min(max(50 * 0.0018 + 0.5, 0), 1))
print("Set up Servos")
max_feedings=setup()
print("Set up Finished. Robot is Ready")
print("Press Button 1 to Empty")
print("Press Button 2 to Close")
print("Press Button 3 to Calibrate")


 
while True:
    # Check button 1 (GP20) is pressed 
    if not btn1.value:
        empty()
        sleep(0.5)
        print("empty")
 
    # Check button 2 (GP21) is pressed
    if not btn2.value: 
        close()
        sleep(0.5)
        print("closed")
        
    # Check button 3 (GP22) is pressed
    if not btn3.value: 
        calibrate()
        sleep(0.5)
    
    # Check if sensor is activated
    if GP2.checkPin(None):
        feed_robot()
        sleep(0.5)






