#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import argparse
from argparse import ArgumentDefaultsHelpFormatter

SAMP_FREQ_HZ = 1e6
DUR_MSEC = 2.0

FREQ_START_HZ = 5000
FREQ_END_HZ = 25000

SPIKE_VOLTS = 3.3
SPIKE_DUR_USEC = 50


def freq_to_count(freq):
    return freq * DUR_MSEC / 1000


def main():

    argparser = argparse.ArgumentParser(
                formatter_class=ArgumentDefaultsHelpFormatter)

    argparser.add_argument('-p', '--plot', action='store_true',
                           help='Plot the signal')

    args = argparser.parse_args()

    n = int(freq_to_count(SAMP_FREQ_HZ))

    t = np.arange(n)

    f1 = freq_to_count(FREQ_START_HZ)

    f2 = freq_to_count(FREQ_END_HZ)

    f = np.linspace(f1, f2, n)

    s = np.sin(2 * np.pi * t *  f / n)

    p = signal.find_peaks(s)[0]

    v = np.zeros(n)
    v[p] = 3.3

    for tval, vval in zip(t, v):
        print('%fm %d' % (tval, vval))

    if args.plot:
        plt.figure(figsize=(20, 6))
        plt.plot(t / 1000, v)
        plt.xlabel('Time (msec)')
        plt.ylabel('Volts')
        plt.show()


main()
