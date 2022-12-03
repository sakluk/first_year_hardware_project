"""
06_rotary_switch_reader.py

***** DRAFT ****
DON'T WORK YET, CHECK FROM JOE WHAT ARE THE SETTINGS FOR SWITCH

First year hardware project
School of ICT
Metropolia University of Applied Sciences
3.12.2022, Sakari Lukkarinen


This demo
- uses interrupts to read the changes in the rotary encoder
- increases or decreases the value of a variable depending in which directon the rotary encoder is turned
- displays the current value of the variable
You can activate the plotter (View > Plotter) to show graphically the values.
"""

# Import libaries
from machine import Pin
import utime

# Rotary coder Pins
C_LEFT = 10
C_RIGHT = 11
C_SWITCH = 12

# Pins for the coder
p1 = Pin(C_LEFT, Pin.IN)
p2 = Pin(C_RIGHT, Pin.IN)
p3 = Pin(C_SWITCH, Pin.IN)

def switch_pressed(pin):
    print('OK')
    
# Coder function
def decode(pin):
    global a0, b0, i
    # Read the pin values
    a = p1.value()
    b = p2.value()
    # Knob is turned left
    if a0 != a:
        i = i - 1
        a0 = a
    # Knob is turned right
    if b0 != b:
        i = i + 1
        b0 = b
    # Print the variable
    print(i)    

# Initialize global variables
a0, b0, c0, i = 0, 0, 0, 0

# Activate interruptions
p1.irq(decode, Pin.IRQ_FALLING)
p2.irq(decode, Pin.IRQ_FALLING)

# Continue until stopped
while True:
    # Read switch button
    c = p3.value()
    if c != c0:
        print(c)
        c0 = c
    # Sleep 100 ms
    utime.sleep_ms(100)
