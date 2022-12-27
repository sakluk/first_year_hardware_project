"""
ADC_demo.py

First year hardware project
School of ICT
Metropolia University of Applied Sciences
12.12.2022, Sakari Lukkarinen

This demo
- Uses and reads data from Analog channel 0 (Pin 26)
- Collects data with given sampling rate (fs samples per second) and given length (L in seconds)
- Writes the raw data to file (filename)

Notes

This demo uses utime.sleep to wait for the next sampling time, and this is not accurate method.
For more accurate timing interrupts should be used. For more details, see:
https://docs.micropython.org/en/latest/reference/isr_rules.html

The demo also prints every D data point to the shell. This can be used to show the collected data
real time in Plotter. For more details, check Thonny: View > Plotter.
"""

import machine
import utime

adc = machine.ADC(26)

filename = 'data_250_005.csv' # Filename to store the data
fs = 250 # sampling rate, samples per second
D = 5 # Decimation factor, used for printing values 
L = 30 # Length of recording, seconds
N = L*fs # Length of recording, samples

# Open the file for writing text
f = open(filename, 'wt', encoding = 'utf-8')

# First write the sampling frequency
f.write(f'fs = {fs} Hz\n')

# Then the length of the data in samples
f.write(f'N = {N}\n')

# Show starting message
print('Start')

# Collect N samples. 
for n in range(N):
    # Read the analog input
    int_val = adc.read_u16()
    
    # Write the data sample to file
    f.write(f'{int_val} \n')
    
    # Print every D data sample
    if (n % D) == 0:
      print(f'{int_val}')
    
    # Wait for 1/fs seconds
    utime.sleep(1/fs)

# Close the file
f.close()

# Show end message
print('Done.')