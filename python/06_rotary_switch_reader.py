"""
06_rotary_switch_reader.py

***** DRAFT ****
DON'T WORK YET, CHECK FROM JOE WHAT ARE THE SETTINGS FOR SWITCH

First year hardware project
School of ICT
Metropolia University of Applied Sciences
3.12.2022, Sakari Lukkarinen


This demo
- uses interrupts to read the rotary knobs button
- display OK when pressed
"""

# Import libaries
from machine import Pin
import utime

# Rotary coder Pins
C_LEFT = 10
C_RIGHT = 11
C_SWITCH = 12

# Connect switch to pin, use pull-up
# resistor, default value is 1
# When the knob switch is pressed the value
# changes to 0
p3 = Pin(C_SWITCH, Pin.IN, Pin.PULL_UP)

def switch_pressed(pin):
    print('OK')

# Activate interruption
p3.irq(switch_pressed, Pin.IRQ_FALLING)

# Continue until stopped
while True:
    # Sleep 100 ms
    utime.sleep_ms(100)
