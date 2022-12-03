"""
09_button_reader.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
3.12.2022, Sakari Lukkarinen


This demo
- reads the microbuttons
"""

# Import libaries
from machine import Pin
import utime

# Rotary coder Pins
C_LEFT = 10
C_RIGHT = 11
C_SWITCH = 12

SW_0 = 9
SW_1 = 8
SW_2 = 7

# Connect pins to the buttons
# Use pull-up resistors, default value is 1
# When button is pressed it changes to 0
b0 = Pin(SW_0, Pin.IN, Pin.PULL_UP)
b1 = Pin(SW_1, Pin.IN, Pin.PULL_UP)
b2 = Pin(SW_2, Pin.IN, Pin.PULL_UP)

def button_0(pin):
    print('Button 0 pressed.')
    
def button_1(pin):
    print('Button 1 pressed.')

def button_2(pin):
    print('Button 2 pressed.')

# Activate interruptions
b0.irq(button_0, Pin.IRQ_FALLING)
b1.irq(button_1, Pin.IRQ_FALLING)
b2.irq(button_2, Pin.IRQ_FALLING)

# Continue until stopped
while True:
    # Sleep 100 ms
    utime.sleep_ms(100)
