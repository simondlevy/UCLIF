This directory contains an Arduino sketch for generating pulses suitable 
for input to the UCLIF neuron circuit.  The sketch reads from a 
potentiometer and converts the reading into a spiking frequency within
a range specified by the parameters at the top of the sketch.   I've
tested this sketch on a Teensy 4.0, but it should run on any 
Arduino-compatible microcontroller that is fast enough to support 
the microsecond resolution used by the sketch.
