"""
02_adc_reading.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
3.12.2022, Sakari Lukkarinen

Original project: 
https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

This demo
- reads continuously the analog channel 0
- converts the integer values to voltage values (analog voltage between 0.0 V and 3.3 V), and
- prints the values in the Shell.
You can activate the plotter (View > Plotter) to show graphically the values.
"""

# Read libraries
from machine import ADC, Pin
import utime

# Analog Pin values
A0 = 26
A1 = 27

# Sampling frequency 25 Hz
fs = 25

# Conversion factor
factor = 3.3/2**16

# Initialize ADC
adc = ADC(Pin(A0))

# Read until stopped
while True:
    
    # Read the analog value and conver the value between 0 and 1
    y = factor*adc.read_u16()
    
    print(y)
    
    # Wait for the sampling period
    utime.sleep(1/fs)