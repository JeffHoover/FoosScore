# FoosScore Notes:

Looking down in the return mechanism from goal (bottom left) to divider (top right).  
https://drive.google.com/open?id=0B_L_-4oFZoGKWkIxRDVIUFJCWGc


Another view of the divider. Goals coming in from both sides. Ball is routed to bottom left of image.  
https://drive.google.com/open?id=0B_L_-4oFZoGKNUctdHZZRVNIU3c

Inside the ball return. Scoop from goal is on the right.  
Ball hits vertical divider in lane at left of photo and rolls to the goal exit out the bottom of the image.  
https://drive.google.com/open?id=0B_L_-4oFZoGKQ0dQbm5JWkJZMmc

A video of the mechanism working is here:  
https://drive.google.com/open?id=0B_L_-4oFZoGKWHkxTjZSdkJuQm8 

The table lock. There is one on each side of the front of the table. Popped out equals unlocked.  
Key is kept in the ball return slot.  
https://drive.google.com/open?id=0B_L_-4oFZoGKUkQ1eEt6bzRDN3M


I’m using my iPhone as a personal hotspot so that I can easily connect my Mac to my headless Pi.

I currently have a model A, but I’ve ordered a 3 B because the A only has one USB port

As a proof of concept, I first got a python program to change the state of an LED whenever a beam is interrupted/restored. 
I used this: http://osoyoo.com/2015/04/03/photo-interrupter-module/ because my IR detector works (I tested it 
using a TV remote) but the IR LED emitter is burned out. I ordered multiple pairs of LED/detector.

NOTE: My IR LED may not be burned out. I learned from here: https://learn.adafruit.com/ir-sensor that 
IR detectors are different from photocells, as they don’t look for presence/absence of IR but rather presence/absence 
of IR modulated at 38 KHz.
Grrr. Doing that on a Pi might be difficult. It may be better suited to an Arduino. No reason the 2 can’t work in conjunction.

Instead of going the IR route, I ordered some ordinary photocells: 
https://www.amazon.com/gp/product/B00H4ZSGXC/ref=oh_aui_detailpage_o00_s00 I have a bunch of visible yellow and 
visible red LEDs that I’m going to try and use.

Code is on github:
https://github.com/JeffHoover/FoosScore 

Some reference links:  
- http://pi4j.com/pins/model-a-plus.html  
- http://osoyoo.com/2015/03/11/osoyoo-sensor-modules-kit-for-arduino/  
- https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api  

GPIO (especially pull-ups and pull-downs):  
http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/ 

I have a display unit like this that can display 00 00 to 99 99 (or most any combination of 4 alphanum characters):  
https://learn.adafruit.com/adafruit-led-backpack/0-54-alphanumeric

For the display to work,  I2C must be enabled on the Pi:  
http://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/

A video of the score counting sequence is here:  
https://drive.google.com/open?id=0B_L_-4oFZoGKVXVIOTRjbDFkNFE

Another video, this one showing me using a TV remote to simulate an optical detection:  
https://drive.google.com/file/d/0B3vuNKvd_BySaktwbWRyZkZYSmw2enZpM1R5UHZaaTJGTUJv/view?usp=sharing 

I have some removable adhesive putty that I’m going to try to use to stick parts onto the inside of the table:   
https://www.amazon.com/Blue-Reusable-Adhesive-Putty-1-Ounce/dp/B005LRTUQ2 

## Working on making the score machine talk  
To make a machine recording of speech into a wav, do this:
flite -t "aaa goal, team 2" -o goal2.wav  
Then in the code, shell out like this:  
os.system("aplay win1.wav")  # this plays synchronously, which slows things down  
Maybe I can find a library to play a asynchronous sound  
In the mean time, I can get asynchrony like this:  
subprocess.Popen(["aplay", "goal1.wav"])  
https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/fun-applications  
http://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python  
If the Pi is connected by HDMI to a monitor, sound will play out of it, unless  
the Pi has something like this:  
https://www.amazon.com/gp/product/B00NLO9JB8/ref=oh_aui_detailpage_o01_s01  
plugged into the headphone jack.


## Possible Extensions of the Project:
- Get 2 photocells / photoresistors detecting a ball
- Get photocells / resistors (non-destructively) installed in the table.
- Route display wires ( through goal or ball return) onto table rim.
- Build another display, but with right-angle pins for ease of mounting
- Amazon Alexa integration
- Raspberry Pi camera inside table to show workings
- Buy, assemble, integrate a LCD display like this: https://www.amazon.com/ADAFRUIT-INDUSTRIES-WHITE-KEYPAD-RASPBERRY/dp/B00DK2A1KE  

Don't boot into GUI?  
What's the cmd line command to boot ui?  

## Alexa Tutorials
- https://medium.com/@jjbskir/unit-testing-an-amazon-alexa-skill-with-node-js-and-jasmine-98982544471f
- https://bespoken.tools/blog/2016/10/10/unit-testing-alexa-skills
- https://www.bignerdranch.com/blog/developing-alexa-skills-locally-with-nodejs-setting-up-your-local-environment/




