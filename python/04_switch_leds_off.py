"""
04_switch_leds_off.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
2.12.2022, Sakari Lukkarinen

Switch all LEDs off. Might be needed after previous demo.
"""

# Import libraries
import utime
from machine import Pin, Timer

# Pin numbers for the LEDs
D0 = 25 # Pico's LED
D1 = 22 # Protoboard's LED1
D2 = 21 # Protoboard's LED2
D3 = 20 # Protoboard's LED3

# Create Pin objects
led0 = Pin(D0, Pin.OUT)
led1 = Pin(D1, Pin.OUT)
led2 = Pin(D2, Pin.OUT)
led3 = Pin(D3, Pin.OUT)

# Switch LED lights off
led0.value(0)
led1.value(0)
led2.value(0)
led3.value(0)