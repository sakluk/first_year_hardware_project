"""
11_real_time_signal_filtering.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
4.12.2022, Sakari Lukkarinen


This demo
- Reads the analog signal using Timer
- The data is stored into a circular buffer having memory of 1024 samples
- When there is enough new data the signal is filtered
- The filtered signal is shown in the OLED display
- The rotary coder's switch can be used to stop the timer
Notes
- This code needs that a special firmware of MicroPython needs to be loaded to Pico.
- How to, see: https://github.com/sakluk/first_year_hardware_project/blob/main/ulab_installation.md
"""

# Import libaries
from machine import Pin, PWM, ADC, I2C, Timer
import utime
import ssd1306
import sys
from ulab import numpy as np
from ulab import scipy
# import network


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



# Template function for rotary encoder button
def rc_button_pressed(pin):
    global tim
    tim.deinit()
    print('Stop recording.')
    oled.fill(0)
    oled.show()
    print('Done')
    sys.exit(0)
    
# Activate interruption for rotary encoder button
rc_button.irq(rc_button_pressed, Pin.IRQ_FALLING)

def display_start_message():
    oled.fill(0)
    # Write text to OLED
    oled.text('Hardware project', 1, 1)
    oled.text('School of ICT', 1, 11)
    oled.text('Metropolia UAS', 1, 21)
    oled.text('3.12.2022', 1, 31)
    #oled.text('----------------', 1, 41)
    oled.text('Welcome!', 1, 48)
    # Draw rectangles around the last numbers
    oled.rect(0, 41, 128, 23, 2)
    oled.rect(0, 42, 128, 21, 2)
    oled.show()
    # Wait for 5 seconds
    utime.sleep(5)
    # Clear the display
    oled.fill(0)
    oled.show()
    # Wait for 1 second
    utime.sleep(1)

def read_filter(fs):
    if fs == 100:
        sos = np.array([[0.15160152,0.17150393,0.15160152,1.00000000,-0.23790607,0.10046022],
            [1.00000000,-0.47152922,1.00000000,1.00000000,-0.79543088,0.63662529],
            [0.92117099,-1.84234199,0.92117099,1.00000000,-1.88660958,0.89033974],
            [1.00000000,-2.00000000,1.00000000,1.00000000,-1.94921596,0.95306990]])
        return sos
    elif fs == 200:
        sos = np.array([[0.09292690,-0.03014272,0.09292690,1.00000000,-1.00702281,0.30503975],
            [1.00000000,-1.55971254,1.00000000,1.00000000,-1.54774667,0.77779276],
            [0.95978223,-1.91956446,0.95978223,1.00000000,-1.94263823,0.94359728],
            [1.00000000,-2.00000000,1.00000000,1.00000000,-1.97526963,0.97624479]])
        return sos
    else:
        return []

# Settings for sampling
fs = 200 # Sampling frequency (Hz)

# Display the start texts
display_start_message()

# Read filter
sos = read_filter(fs)
if sos == []:
    sys.exit('Ahaa! Filter reading does not work.')
# print('Filter coefficients read.')
# print('Shape of sos:', sos.shape)
# print(sos)

input_buf = np.zeros(1024, dtype = np.uint16)
N = 0
def read_signal(tim):
    global input_buf, N
    x = adc0.read_u16()
    input_buf[N] = x
    N += 1
    N = N % 1024
    if N % 256 == 0:
        filter_signal(input_buf, N)

zi = np.zeros((4, 2))        
def filter_signal(x, N):
    global zi
    if N == 0:
        y, zi = scipy.signal.sosfilt(sos, x[-256:], zi = zi)
    else:
        y, zi = scipy.signal.sosfilt(sos, x[N-256:N], zi = zi)
    display_signal(y)
    
def display_signal(y):   
    oled.fill(0)
    for n in range(len(y)-1):
        x1 = int((n + 1)//2)
        x2 = int((n + 2)//2)
        y1 = int(-y[n]//512 + 32)
        y2 = int(-y[n+1]//512 + 32)
        oled.line(x1, y1, x2, y2, 3)
    oled.show()


tim = Timer()
tim.init(period = 1000//fs, callback = read_signal)

utime.sleep(10)
sys.exit(0)
# Should be done something after sleep time is over. Timer is still working.

