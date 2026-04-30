#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

NSAMP = 5000
FREQ_START = 2
FREQ_END = 10

t = np.arange(NSAMP)

v = np.sin(2 * np.pi * t * np.linspace(FREQ_START, FREQ_END, NSAMP) / NSAMP)

plt.plot(t, v)
plt.show()
