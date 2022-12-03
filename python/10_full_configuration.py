"""
10_full_configuration.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
3.12.2022, Sakari Lukkarinen


This demo combines all the codes used so far.
- Reads the analog signal
- Scales it to fit into to the OLED display
- Reads buttons and rotary encoder
- Blinks LEDs when microbuttons are pressed
Notes
- There comes several interruptions when microbuttons are pressed.
"""

# Import libaries
from machine import Pin, PWM, ADC, I2C
import utime
import ssd1306

# Analog inputs
A0 = 26 # Analog input 0
A1 = 27 # Analog input 1

# LEDs
D0 = 25 # Pico's LED
D1 = 22 # Protoboard's LED1
D2 = 21 # Protoboard's LED2
D3 = 20 # Protoboard's LED3

# Rotary coder
C_LEFT = 10
C_RIGHT = 11
C_SWITCH = 12

# OLED
OLED_SCL = 15 # Clock
OLED_SDA = 14 # Data

# Microbuttons
SW_0 = 9
SW_1 = 8
SW_2 = 7

# Analog inputs
adc0 = ADC(Pin(A0))
# adc1 = ADC(Pin(A1))

# LEDs
led0 = Pin(D0, Pin.OUT)
led1 = Pin(D1, Pin.OUT)
led2 = Pin(D2, Pin.OUT)
led3 = Pin(D3, Pin.OUT)

# OLED
i2c_oled = I2C(1, scl=Pin(OLED_SCL), sda=Pin(OLED_SDA), freq=400000)
OLED_WIDTH = 128
OLED_HEIGHT = 64
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c_oled)

# Rotary coder
rc_left = Pin(C_LEFT, Pin.IN)
rc_right = Pin(C_RIGHT, Pin.IN)
rc_button = Pin(C_SWITCH, Pin.IN, Pin.PULL_UP)

# Microbuttons
but0 = Pin(SW_0, Pin.IN, Pin.PULL_UP)
but1 = Pin(SW_1, Pin.IN, Pin.PULL_UP)
but2 = Pin(SW_2, Pin.IN, Pin.PULL_UP)


# Template function for rotary coder
RC_L, RC_R, RC_I = 0, 0, 0
def decode(pin):
    global RC_L, RC_R, RC_I
    # Read the pin values
    a = rc_left.value()
    b = rc_right.value()
    # Knob is turned left
    if a != RC_L:
        RC_I -= 1
        RC_L = a
    # Knob is turned right
    if b != RC_R:
        RC_I += 1
        RC_R = b
    # Print the value
    print(f'Rotary coder value: {RC_I}')

# Activate interruptions for rotary coder
rc_left.irq(decode, Pin.IRQ_FALLING)
rc_right.irq(decode, Pin.IRQ_FALLING)

# Template function for rotary encoder button
def rc_button_pressed(pin):
    print('Rotary coder button pressed.')

# Activate interruption for rotary encoder button
rc_button.irq(rc_button_pressed, Pin.IRQ_FALLING)

# Template functions for microbuttons
def button_0(pin):
    print('Button 0 pressed.')
    led0.toggle()
    
def button_1(pin):
    print('Button 1 pressed.')
    led1.toggle()
    
def button_2(pin):
    print('Button 2 pressed.')
    led2.toggle()

# Activate interruptions for microbuttons
but0.irq(button_0, Pin.IRQ_FALLING)
but1.irq(button_1, Pin.IRQ_FALLING)
but2.irq(button_2, Pin.IRQ_FALLING)


# Scaler function to display the signal on the OLED
def scale_signal_for_display(x):
    global gain, offset
    # Scale and offset are given in scale 2**16 = 65536
    # Then scale down to 2**6 = 64
    y = (gain*x - offset) // 1024
    # Limit low values to 0
    y = max(y, 0)
    # Limit high values to 64
    y = min(y, 64)
    return y

# Displays and updates the graph shown on the OLED
def display_signal(y):
    global x0, y0, n
    # Take the modulus
    x = n % 129
    # Reset the display, when 128 pixels are used
    if x == 0:
        oled.fill(0)
        x0 = 0
    # Draw a line segment
    # Turn the y-axis upside down, as the origio (0,0) is in the upper left corner
    oled.line(x0, 64-y0, x, 64-y, 1)
    oled.show()
    # Update line segment starting point
    x0 = x
    y0 = y


# Settings for sampling
fs = 100 # Sampling frequency (Hz)
gain = 2 # for scaling raw analog signal
offset = 46000 # for offsettin raw analog signal

# Initial values for graphing
x0, y0, n = 0, 0, 0

# Continue until stopped
while True:
    # Read the analog signal
    y_raw = adc0.read_u16()
    # Increase number of values read
    n += 1
    # Scale the signal down to scale between 0 and 64
    y = scale_signal_for_display(y_raw)    
    # Show the signal on the OLED
    display_signal(y)
    # Print the value (for debugging)
    # print(y)
 
    # Sleep for the sampling period time
    utime.sleep(1/fs)
