#!/usr/bin/python

import Adafruit_CharLCD as LCD
import sys
import time

#print sys.argv[2]

lcd_columns = 16

lcd = LCD.Adafruit_CharLCDPlate()

lcd = LCD.Adafruit_CharLCDPlate()
if sys.argv[2] == "red":
    lcd.set_color(1.0, 0.0, 0.0)
if sys.argv[2] == "green":
    lcd.set_color(0.0, 1.0, 0.0)
if sys.argv[2] == "blue":
    lcd.set_color(0.0, 0.0, 1.0)
if sys.argv[2] == "yellow":
    lcd.set_color(1.0, 1.0, 0.0)
if sys.argv[2] == "cyan":
    lcd.set_color(0.0, 1.0, 1.0)
if sys.argv[2] == "magenta":
    lcd.set_color(1.0, 0.0, 1.0)
if sys.argv[2] == "white":
    lcd.set_color(1.0, 1.0, 1.0)

lcd.clear()
message = sys.argv[1]
lcd.message(message)
if lcd_columns < len(message):
    while(True):
    	for i in range(len(message)-lcd_columns):
            time.sleep(1)
            lcd.move_left()
    	for i in range(len(message)-lcd_columns):
            time.sleep(1)
            lcd.move_right()


