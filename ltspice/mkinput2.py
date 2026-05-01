#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import argparse
from argparse import ArgumentDefaultsHelpFormatter

DUR_MSEC = 2.0

def freq_to_count(freq):
    return freq * DUR_MSEC / 1000


def main():

    parser = argparse.ArgumentParser(
                formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('-p', '--plot', action='store_true',
                           help='Plot the signal')

    parser.add_argument('-v', '--vmax', default=3.3,
            type=float, help='Max voltage')

    parser.add_argument('-f', '--fsamp', default=1e6,
            type=float, help='Sampling freq (hz)')

    parser.add_argument("f_beg", help="Beginning frequency", type=float)
    parser.add_argument("f_end", help="Ending frequency", type=float)
    parser.add_argument("s_dur", help="Spike duration in msec", type=float)

    args = parser.parse_args()

    n = int(freq_to_count(args.fsamp))

    t = np.arange(n)

    f1 = freq_to_count(args.f_beg)

    f2 = freq_to_count(args.f_end)

    f = np.linspace(f1, f2, n)

    s = np.sin(2 * np.pi * t *  f / n)

    p = signal.find_peaks(s)[0]

    v = np.zeros(n)
    v[p] = args.vmax

    # for tval, vval in zip(t, v):
    #     print('%fm %d' % (tval, vval))

    if args.plot:
        plt.figure(figsize=(20, 6))
        plt.plot(t / 1000, v)
        plt.xlabel('Time (msec)')
        plt.ylabel('Volts')
        plt.show()


main()
