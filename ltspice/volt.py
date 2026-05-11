#!/usr/bin/python3
'''
   Python script to generate a voltage-coded PWL file for use as input to
   the UCLIF neuron

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
from sys import argv

FSAMP = 1e6

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
                epilog='Example: %s 1 5 15 10 -p' % argv[0])

    parser.add_argument('-p', '--plot', action='store_true',
                           help='Plot the signal')

    parser.add_argument('-s', '--step', action='store_true',
                           help=('Step directly from high to low voltage ' +
                                'at halfway point (no ramp)'))

    parser.add_argument('-f', '--freq', default=2000,
            type=float, help='Spiking frequency (Hz)')

    parser.add_argument('-o', '--outfile', default='pulse.txt',
            help='Output file name')

    parser.add_argument("v_beg", help="Beginning voltage", type=float)
    parser.add_argument("v_end", help="Ending voltage", type=float)
    parser.add_argument("t_dur", help="Total duration in msec", type=float)
    parser.add_argument("s_dur", help="Spike duration in usec", type=float)

    args = parser.parse_args()

    n = int(freq_to_count(FSAMP, args))

    t = np.arange(n)

    f = freq_to_count(args.freq, args)

    f = np.linspace(f, f, n)

    v = make_spikes(t, f, n, args.s_dur) * np.linspace(args.v_beg, args.v_end, n)

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
