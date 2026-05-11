#!/usr/bin/python3
'''
   Python script to generate a .txt file for use as input to the
   UCLIF neuron

   Copyright (C) 2026 Simon D. Levy

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, in version 3.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http:--www.gnu.org/licenses/>.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import argparse
from argparse import ArgumentDefaultsHelpFormatter

def freq_to_count(freq, args):
    return freq * args.t_dur / 1000


def make_spikes(t, f, n, s_dur):
    s = np.sin(2 * np.pi * t *  f / n)
    v = np.zeros(n)
    halfspike = int(s_dur / 2)
    for k in signal.find_peaks(s)[0]:
        lo = max(0, k-halfspike)
        hi = min(n, k+halfspike+1)
        v[range(lo, hi)] = 1
    return v

def main():

    parser = argparse.ArgumentParser(
                formatter_class=ArgumentDefaultsHelpFormatter,
                description='Make PWL input file for LTSPICE',
                epilog='Example: mkpwl.py 5000 10000 15 10 -p')

    parser.add_argument('-p', '--plot', action='store_true',
                           help='Plot the signal')

    parser.add_argument('-s', '--step', action='store_true',
                           help=('Step directly from high to low frequency ' +
                                'at halfway point (no ramp)'))

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

    if args.step:
        f1 = np.linspace(f1, f1, n)
        v1 = make_spikes(t, f1, n, args.s_dur)
        f2 = np.linspace(f2, f2, n)
        v2 = make_spikes(t, f2, n, args.s_dur)
        v1 = v1[:n//2]
        v2 = v2[:n//2]
        v = np.append(v1, v2)

    else:
        f = np.linspace(f1, f2, n)
        v = make_spikes(t, f, n, args.s_dur)

    v *= args.vmax

    with open(args.outfile, 'w') as fp:
        for tval, vval in zip(t, v):
            fp.write('%fm %f\n' % (tval/1000, vval))

    print('Wrote ' + args.outfile)

    if args.plot:

        plt.figure(figsize=(20, 6))

        plt.plot(t / 1000, v)
        plt.xlabel('Time (msec)')

        plt.ylabel('Volts')
        plt.show()


main()
