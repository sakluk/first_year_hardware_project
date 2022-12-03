"""
03_heart_beat_indicator.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
3.12.2022, Sakari Lukkarinen

Original project: 
https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8

This demo
- reads continuously the analog channel
- scales and offset the values
- controls the brightness of the LED using PWM
- prints the duty cycle value (uint16) 
You can activate the plotter (View > Plotter) to show graphically the values.
"""
from machine import Pin, PWM, ADC
import utime

# Pin numbers for the LEDs
D0 = 25 # Pico's LED
D1 = 22 # Protoboard's LED1
D2 = 21 # Protoboard's LED2
D3 = 20 # Protoboard's LED3

# Analog Pin values
A0 = 26
A1 = 27

# Sampling frequency 25 Hz
fs = 25

# Gain and offset
gain = 2
offset = 46000

# Analog input and PWM control (LED)
adc = ADC(Pin(A0))
pwm = PWM(Pin(D1))
pwm.freq(1000)
pwm.duty_u16(0)

# Loop until stopped
while True:
    # Read the analog signal
    aint = adc.read_u16()
    # Scale and offset
    duty = gain*aint - offset
    # Limit low values to 0
    duty = max(duty, 0)
    # Limit high values to 2**16
    duty = min(duty, 65536)
    # Change the duty cycle
    pwm.duty_u16(duty)
    # Print the value
    print(duty)
    # Sleep for sampling period
    utime.sleep(1/fs)