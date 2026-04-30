#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

SAMP_FREQ_HZ = 1e6
DUR_MSEC = 2.0

FREQ_START_HZ = 10  # 2
FREQ_END_HZ= 10

SPIKE_VOLTS = 3.3
SPIKE_DUR_USEC = 50

n = int(SAMP_FREQ_HZ * DUR_MSEC / 1000)

t = np.arange(n)

f = np.linspace(FREQ_START_HZ, FREQ_END_HZ, n)

s = np.sin(2 * np.pi * t *  f / n)

p = signal.find_peaks(s)[0]

v = np.zeros(n)
v[p] = 3.3

plt.figure(figsize=(20, 6))
plt.plot(t / 1000, v)
plt.xlabel('Time (msec)')
plt.ylabel('Volts')
plt.show()
