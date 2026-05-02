#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import argparse
from argparse import ArgumentDefaultsHelpFormatter

def freq_to_count(freq, args):
    return freq * args.t_dur / 1000


def main():

    parser = argparse.ArgumentParser(
                formatter_class=ArgumentDefaultsHelpFormatter,
                description='Make PWL input file for LTSPICE',
                epilog='Example: mkpwl.py 5000 5000 15 10 -p')

    parser.add_argument('-p', '--plot', action='store_true',
                           help='Plot the signal')

    parser.add_argument('-v', '--vmax', default=3.3,
            type=float, help='Max voltage')

    parser.add_argument('-f', '--fsamp', default=1e6,
            type=float, help='Sampling freq (hz)')

    parser.add_argument('-o', '--outfile', default='pulse.txt',
            help='Output file name')

    parser.add_argument("f_beg", help="Beginning frequency", type=float)
    parser.add_argument("f_end", help="Ending frequency", type=float)
    parser.add_argument("t_dur", help="Total duration in msec", type=float)
    parser.add_argument("s_dur", help="Spike duration in usec", type=float)

    args = parser.parse_args()

    n = int(freq_to_count(args.fsamp, args))

    t = np.arange(n)

    f1 = freq_to_count(args.f_beg, args)

    f2 = freq_to_count(args.f_end, args)

    f = np.linspace(f1, f2, n)

    s = np.sin(2 * np.pi * t *  f / n)

    v = np.zeros(n)

    half = int(args.s_dur / 2)

    for k in signal.find_peaks(s)[0]:
        lo = max(0, k-half)
        hi = min(n, k+half+1)
        v[range(lo, hi)] = args.vmax

    with open(args.outfile, 'w') as fp:
        for tval, vval in zip(t, v):
            fp.write('%fm %f\n' % (tval/1000, vval))

    print('Wrote ' + args.outfile)

    if args.plot:

        plt.figure(figsize=(20, 6))

        plt.plot(t / 1000, v)
        plt.xlabel('Time (msec)')

        plt.xlim([0,1.5])

        plt.ylabel('Volts')
        plt.show()


main()
