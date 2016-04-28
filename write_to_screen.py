#!/usr/bin/python

import Adafruit_CharLCD as LCD
import sys
import time

lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
lcd.message(sys.argv[1])

