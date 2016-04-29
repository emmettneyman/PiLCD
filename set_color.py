#!/usr/bin/python

import Adafruit_CharLCD as LCD
import sys
import time

lcd_columns = 16
print sys.argv[1]
lcd = LCD.Adafruit_CharLCDPlate()
if sys.argv[1] == "red":
    lcd.set_color(1.0, 0.0, 0.0)
if sys.argv[1] == "green":
    lcd.set_color(0.0, 1.0, 0.0)
if sys.argv[1] == "blue":
    lcd.set_color(0.0, 0.0, 1.0)
if sys.argv[1] == "yellow":
    lcd.set_color(1.0, 1.0, 0.0)
if sys.argv[1] == "cyan":
    lcd.set_color(0.0, 1.0, 1.0)
if sys.argv[1] == "magenta":
    lcd.set_color(1.0, 0.0, 1.0)
if sys.argv[1] == "white":
    lcd.set_color(1.0, 1.0, 1.0)
