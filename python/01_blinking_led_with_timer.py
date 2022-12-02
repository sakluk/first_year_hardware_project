"""
01_blinking_led_with_timer.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
2.12.2022, Sakari Lukkarinen

Original source: 
https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5

This demo blinks all LEDs in the protoboard for 10 seconds.
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

# Create timers
timer0 = Timer()
timer1 = Timer()

# Toggle Pico's LED
def blink0(timer):
    led0.toggle()

# Toggle Protoboard's LEDs
def blink1(timer):
    global n
    n += 1
    i = n % 3
    if i == 1:
        led1.toggle()
    elif i == 2:
        led2.toggle()
    else:
        led3.toggle()

# Initialize timers and counter n
n = 0
timer0.init(freq=2.5, mode=Timer.PERIODIC, callback=blink0)
timer1.init(freq=7.5, mode=Timer.PERIODIC, callback=blink1)

# Wait for 10 seconds and then turn the timers off
utime.sleep(10)
timer0.deinit()
timer1.deinit()

# Switch LED lights off
led0.value(0)
led1.value(0)
led2.value(0)
led3.value(0)