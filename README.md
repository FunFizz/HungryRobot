# HungryRobot
Make a Hungry Robot with **Cytron Maker Pi Pico board**, a distance sensor and a servo.  

This is based on the tutorial presented at **https://www.youtube.com/watch?v=KfP_LfUiwdc** as suggested by Michael Creggan.

Funding has been provided curtesy of the Teaching Innovation Fund.

**TARGET AUDIENCE:**  P6/P7 Children
**SCHOOLS:** Possibly Fane Primary School
****GROUP SIZE:** 20
LENGTH OF WORKSHOP**: 90 minutes
**VENUE:** Farset Labs?
**DATE:** TBA - need to Book
**TIME:** TBA

**TO DO:**  
**LEARNING OBJECTIVES**
**PURPOSE** linked to research
**BENEFITS** including LINK TO **CURRICULUM CCEA** and the stages
PHOTO/VIDEO PERMISSION FORMS
FOOD ALLERGIES AND MEDICAL/LEARNING ETC REQUIREMENTS
FOOD
RISK ASSESSMENT
BADGES
TUTORIAL
GITHUB
EVALUATION FORMS
WEB SITE - EVENT ANNOUNCEMENT

**HARDWARE:**

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/aada5d81-5e34-48e9-bf88-5563fa58e32b)  More information on the Cytron Maker Pi Pico Board can be found here: ** https://github.com/CytronTechnologies/MAKER-PI-PICO/tree/main**.

Cytron Maker Pi Pico Board [donated by Michael Creggan] x 1
USB Micro B cable x 1
IR distance Sensors x 1
Servos x 1
Cable Ties x 10
Googly Eyes x 2
Screwdriver x 1
Screws
Blue Tack
Glue Dots

**3D FILES**
https://www.thingiverse.com/thing:2824451
![image](https://github.com/FunFizz/HungryRobot/assets/97193087/96189025-2c8b-4f29-8967-dc56c3f76ca2)
From top left to bottom right we have:
1. Bottom
2. Hand
3. Head
4. Inner Body
5. Linked
6. New Body

**SOFTWARE**
Go to makeplaypiper (https://make.playpiper.com/).  Copy the block code given below (Pythin Code in Folder).

**B:  CONNECTING THE SOFTWARE TO THE HARDWARE:**  I have connected the analog servo to Grove 1 and the IR detector to Grove 6 (for analog/use Grove 4 for digital example whilst using the prototype code).
makeplaypiper (https://make.playpiper.com/)

I have also tried out  which has the advantage of seeing the code alongside this.  The great advantage of using this board is the great sound it produces.

<img width="378" alt="my_Hungry Robot (2)" src="https://github.com/FunFizz/HungryRobot/assets/97193087/fc3c1ae0-2e54-436f-a57e-c40597bdae5e">

_________________________________________________________________________________________________________________________
**TEACHER NOTES**

**FEATURES OF THE CYTRON MAKER Pi PICO**
You can see the features of the Cytrin Make Pi PICO on the table below on the right hand column.  The robotics board on the left also looks very interesting.

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/b265dc63-0c5b-4bdf-9e70-efd4af731cb7)

**ALTERNATIVE IDEs**

**THONNY**

The Thonny app is the orginal suggestion:  **https://thonny.org/**
 
**A:  SETTING UP MICROPYTHON:**  I have orginally added prototype code for Micropython.  To use Micropython on the board I choose Configure Interpreter from the Run Menu.  I selected Micropython Raspberry Pi Pico as the interpreter and tried to detect the port automatically.  I clicked on the link Install or Update Micropython.  It tells you to plug in the board while pressing the BOOTSEL button on the green Pico board to enter bootlaoder mode and then you can select the version of MicroPython you require. Once finished unplug the board and plug it in normally and you shoudl see the status message on the bottom right of the screen which teels you the language and the COM port.  

 ![image](https://github.com/FunFizz/HungryRobot/assets/97193087/f2505a6a-32d5-4f3b-a7ec-7c321979a03a)
![image](https://github.com/FunFizz/HungryRobot/assets/97193087/278d630f-e1c4-493c-98d1-3d7383052894)
[image](https://github.com/FunFizz/HungryRobot/assets/97193087/d03005bc-e632-4852-94be-0b9930720bed)

**RUNNING THE SOFTWARE:**
Chose Save as from the File Menu and then save the code on your computer and do again but this time store on the raspberry pico.  Press Play to run and end the script with Stop.  

**BLOCK CODING**

**LANGUAGE:**  Micropython or Circuit Python or Block Coding? It may be useful to evaluate other methods to code using blocks for instance using: https://wokwi.com/pi-pico or https://mindplus.dfrobot.com/
Evaluate benefits of teaching hands on.

I have for example set up the sensor and the servo to work together on MicroBlocks..You can see how to install the software on the board here:  http://microblocks.fun/get-started#board 

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/9c022109-1c1f-4207-84a5-db175a6202a3)

**ARDUINO CODE**
Example code provided for Arduino :  https://github.com/happythingsmaker/TrashEatingRobot 

**OTHER INSPIRATION**: https://www.cytron.io/tutorial/diy-piano-paper-with-raspberry-pi-pico 

_________________________________________________________________________________________________________________________
**EVALUATION**


