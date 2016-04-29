#!/usr/bin/python

import Adafruit_CharLCD as LCD
import sys
import time

lcd_columns = 16

lcd = LCD.Adafruit_CharLCDPlate()

lcd.clear()
message = sys.argv[1]
lcd.message(message)
while(True):
    for i in range(len(message)-lcd_columns):
        time.sleep(1)
        lcd.move_left()
    for i in range(len(message)-lcd_columns):
        time.sleep(1)
        lcd.move_right()


