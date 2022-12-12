""""
filter_speed_test
28.11.2022, Sakari Lukkarinen
Hardware 2 project
School of ICT
Metropolia University of Applied Sciences

The aim of this code is to test how fast we can run digital filtering with Pico. The code uses ulab library and
requires that a special firmware of MicroPython compiled with ulab should be used.

The code generates a test signal of length N having a unit impulse at the beginning and a unit step at the middle
of the signal. The filter is the 4th order Chebychev II type bandbass filter having corner frequencies of 0.5 and
20 Hz and sampling frequency fs = 1 kHz. The filter is given in second-order-sections (SOS) format. The filter is
designed with scipy.signal.cheby() function.

The code uses ulab's scipy.signal.sosfilt() to filter the signals. First the whole test signal x is given to the
filter once and the total time and time per sample are calculated. Then the signal is given in slices of length L
to the filter and the times are compared to the whole signal filtering.

The best approach for real signal processing application is to use long enough signal slices as the time per sample
increases rather quickly when the length of slice is decreased. Here is the summary of test results run on RPI Pico
with Thonny:

All 10000 samples at once:
Total time =    318 ms
per sample =   31.8 us

=======================
Samples Total  Time per
per     time   sample
step    (ms)   (us)
-----------------------
1000     345    34.5
 500     351    35.1
 250     357    35.7
 100     389    38.9
  50     436    43.6
  25     534    53.4
  10     826    82.6
   5    1313   131.3
   2    2771   277.1
   1    5220   522.2
========================
"""

# Read libraries and functions
from ulab import numpy as np
from ulab import scipy as scipy
from utime import sleep_ms, ticks_ms, ticks_diff

# Initialize input and output arrays
# Input array has a unit impulse at the beginning and unit step at the middle of the array 
N = 10000 # samples in test signal
L = 10 # length of samples filtered by one step
x = np.zeros(N) # input signal
x[0] = 1 # unit impulse
x[N//2:] = 1 # unit step
y = np.zeros(N) # output signal

# Second order systems used for filtering
# designed with scipy in Jupyterlab using the following specifications
# from scipy import signal
# fs = 1000
# N = 4
# rp = 0
# rs = 40
# Wn = [0.5, 20]
# btype = 'bandpass'
# output = 'sos'
# sos = signal.cheby2(N, rs, Wn, btype, False, output, fs)
sos = np.array([
    [ 0.00948267, -0.01800798,  0.00948267,  1.,         -1.88883657,  0.89287328],
    [ 1.,         -1.98166744,  1.,          1.,         -1.95779339,  0.96218095],
    [ 1.,         -1.99999849,  1.,          1.,         -1.98952777,  0.98956418],
    [ 1.,         -1.99999152,  1.,          1.,         -1.99656361,  0.99659845]])
# Initial values for delays
zi = np.ones((4,2))

# Calculate time for filtering the whole signal at once
t0 = ticks_ms()
y = scipy.signal.sosfilt(sos, x)
t1 = ticks_ms()
dt = ticks_diff(t1, t0)

print(f'All {N} samples at once:')
print(f'Total time = {dt:7.2f} ms')
print(f'per sample = {1000*dt/N:7.2f} us')
print('')

# Calculate time for filtering the signal sample by sample
t0 = ticks_ms()
for n in range(0, N, L):
    y[n:n+L], zo = scipy.signal.sosfilt(sos, x[n:n+L], zi = zi)
    zi = zo
t1 = ticks_ms()
dt = ticks_diff(t1, t0)

print(f'{L} sample(s) per step:')
print(f'Total time = {dt:7.2f} ms')
print(f'per sample = {1000*dt/N:7.2f} us')
print('')

