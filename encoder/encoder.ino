static const uint8_t OUTPUT_PIN = 9;

static const uint32_t SPIKE_DURATION_USEC = 500;

const uint32_t FREQ_HZ = 40;

void setup()
{
    pinMode(OUTPUT_PIN, OUTPUT);
}

void loop()
{ 
    const auto usec_curr = micros();
    static uint32_t _usec_prev;

    // Spike at an interval determined by FREQ_HZ 
    if (usec_curr - _usec_prev > 1'000'000/FREQ_HZ) {

        digitalWrite(OUTPUT_PIN, HIGH);
        delayMicroseconds(SPIKE_DURATION_USEC);
        digitalWrite(OUTPUT_PIN, LOW);

        _usec_prev = usec_curr;
    }
}
