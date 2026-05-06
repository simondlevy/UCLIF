/*
   Encoder sketch

   Input: Potentiometer
   Output: Voltage spikes

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
 */


static const uint8_t INPUT_PIN = A9;
static const uint8_t OUTPUT_PIN = 0;

static const uint32_t SPIKE_DURATION_USEC = 10;

static const float FREQ_MIN_HZ = 1000;
static const float FREQ_MAX_HZ = 50'000;

void setup()
{
    pinMode(OUTPUT_PIN, OUTPUT);
}

void loop()
{ 
    const float freq_hz = FREQ_MIN_HZ +
        ((1023 - analogRead(INPUT_PIN)) /1023.f) *
        (FREQ_MAX_HZ - FREQ_MIN_HZ);

    const uint32_t spike_interval_usec = 1'000'000 / freq_hz;

    printf("%d hz | %lu usec\n", (int)freq_hz, spike_interval_usec);

    digitalWrite(OUTPUT_PIN, HIGH);
    delayMicroseconds(SPIKE_DURATION_USEC);
    digitalWrite(OUTPUT_PIN, LOW);

    delayMicroseconds(spike_interval_usec);
}
