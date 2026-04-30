#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

NSAMP = 5000
FREQ_START_HZ = 2
FREQ_END_HZ= 10
SPIKE_VOLTS = 3.3
SPIKE_DUR_USEC = 50

t = np.arange(NSAMP)

f = np.linspace(FREQ_START_HZ, FREQ_END_HZ, NSAMP)

s = np.sin(2 * np.pi * t *  f / NSAMP)

p = signal.find_peaks(s)[0]

v = np.zeros(NSAMP)
v[p] = 3.3

plt.figure(figsize=(20, 6))
plt.plot(t, v)
plt.ylabel('Volts')
plt.show()
