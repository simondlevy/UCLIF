#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(15000)

t100 = t % 200

v = t // 2500 + 2

v[t100>9] = 0

t = t.astype(float) / 1000

plt.plot(t, v)
plt.show()

for tval, vval in zip(t, v):
    print('%fm %d' % (tval, vval))
