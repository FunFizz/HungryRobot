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

Cytron Maker Pi Pico Board donated by Michael Creggan
IR distance Sensors
Servos
Cable Ties

Information on the Cytron Maker Pi Pico Board can be found here: ** https://github.com/CytronTechnologies/MAKER-PI-PICO/tree/main**.

**FILES**
https://www.thingiverse.com/thing:2824451

**SOFTWARE**

Example code provided for Arduino :  https://github.com/happythingsmaker/TrashEatingRobot   

We will need to choose an **IDE** for development purposes.

The Thonny app is the orginal suggestion:  **https://thonny.org/**

 
**A:  SETTING UP MICROPYTHON:**  I have orginally added prototype code for Micropython.  To use Micropython on the board I choose Configure Interpreter from the Run Menu.  I selected Micropython Raspberry Pi Pico as the interpreter and tried to detect the port automatically.  I clicked on the link Install or Update Micropython.  It tells you to plug in the board while pressing the BOOTSEL button on the green Pico board to enter bootlaoder mode and then you can select the version of MicroPython you require. Once finished unplug the board and plug it in normally and you shoudl see the status message on the bottom right of the screen which teels you the language and the COM port.  

 ![image](https://github.com/FunFizz/HungryRobot/assets/97193087/f2505a6a-32d5-4f3b-a7ec-7c321979a03a)
![image](https://github.com/FunFizz/HungryRobot/assets/97193087/278d630f-e1c4-493c-98d1-3d7383052894)
[image](https://github.com/FunFizz/HungryRobot/assets/97193087/d03005bc-e632-4852-94be-0b9930720bed)

**B:  CONNECTING THE SOFTWARE TO THE HARDWARE:**  I have connected the analog servo to Grove 1 and the IR detector to Grove 4 whilst using the prototype code.
![IMG_20231228_100903](https://github.com/FunFizz/HungryRobot/assets/97193087/9777ea8a-8447-4acd-9dbf-c1008a3e3506)

**C: RUNNING THE SOFTWARE:**
Chose Save as from the File Menu and then save the code on your computer and do again but this time store on the raspberry pico.  Press Play to run and end the script with Stop.  

TO DO...RESEARCH
**LANGUAGE:**  Micropython or Circuit Python or Block Coding? It may be useful to evaluate other methods to code using blocks for instance using: https://wokwi.com/pi-pico or https://mindplus.dfrobot.com/
Evaluate benefits of teaching hands on.

I have for example set up the sensor and the servo to work together on MicroBlocks..You can see how to install the software on the board here:  http://microblocks.fun/get-started#board 

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/9c022109-1c1f-4207-84a5-db175a6202a3)

I have also tried out makeplaypiper which has the advantage of seeing the code alongside this.  The great advantage of using this board is the great sound it produces.  Just add sounds:

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/697d98cf-9c82-49f9-95f8-446755babbf8)

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/95f1aa71-b837-48b5-ae23-283ec0c6ab09)

![image](https://github.com/FunFizz/HungryRobot/assets/97193087/e294c6ab-a5d6-4ede-b74f-2f80c8e2ddef)





To DO...EVALUATION
**OTHER INSPIRATION**: https://www.cytron.io/tutorial/diy-piano-paper-with-raspberry-pi-pico 

