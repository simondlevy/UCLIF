static const uint8_t OUTPUT_PIN = 9;
static const uint8_t POT_PIN = A0;

static const uint32_t SPIKE_DURATION_USEC = 500;
const uint32_t FREQ_HZ = 40;

static const uint32_t FREQ_MIN_HZ = 10;
static const uint32_t FREQ_MAX_HZ = 100;

void setup()
{
    pinMode(OUTPUT_PIN, OUTPUT);
}

void loop()
{ 
    // Convert potentiometer input into spiking frequency
    const uint32_t freq_hz =
        map(analogRead(POT_PIN), 0, 1023, FREQ_MIN_HZ, FREQ_MAX_HZ);

    const auto usec_curr = micros();
    static uint32_t _usec_prev;

    // Spike at an interval determined by freq_hz 
    if (usec_curr - _usec_prev > 1'000'000 / freq_hz) {

        digitalWrite(OUTPUT_PIN, HIGH);
        delayMicroseconds(SPIKE_DURATION_USEC);
        digitalWrite(OUTPUT_PIN, LOW);

        _usec_prev = usec_curr;
    }
}
