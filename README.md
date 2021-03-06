# PiLCD
An easy-to-use platform to write to an LCD screen wirelessly using a Raspberry Pi.

##The Inspiration
Often, professors are out of their offices when students come by to talk or ask questions. We wanted to create a device that would allow professors to share quick messages with their students from anywhere on campus.

##The Technology
We used a Raspberry Pi with an Adafruit Character LCD Plate on the hardware side and a simple Flask server paired with an HTML website on the software side. We used the Adafruit Python LCD library to display text on the LCD screen using Python. The Flask server hosted on the Pi handled POST requests sent by the webiste and handled them accordingly. Either the color was set and stored in a global field or the text to be displayed was set and stored. Then, a supplementary Pyhton program was called that would update the screen's color and text accordingly. The screen's color and text could be set instantly and wirelessly anywhere on campus!

##What's Next?
A natural next step for our project would be to collect feedback from people who view messages on the screen. The Adafruit LCD screen has several buttons built in that could be used to send feedback to the owner of the screen. For example, if a professor has the screen displaying the message "Out of the office til 4. Press 'Select' to let me know I missed you", then he could keep track of how many visitors he missed. 

Adafruit LCD Library: https://github.com/adafruit/Adafruit_Python_CharLCD

Video Demo: https://www.youtube.com/watch?v=xQftUTxO4fc

![alt tag](https://raw.githubusercontent.com/emmettneyman/PiLCD/master/PiBlue.jpg)
![alt tag](https://raw.githubusercontent.com/emmettneyman/PiLCD/master/PiGreen.jpg)
![alt tag](https://raw.githubusercontent.com/emmettneyman/PiLCD/master/PiMagenta.jpg)

