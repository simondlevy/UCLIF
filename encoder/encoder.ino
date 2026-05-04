static const uint8_t INPUT_PIN = A9;
static const uint8_t OUTPUT_PIN = 0;

static const uint32_t SPIKE_DURATION_USEC = 50;
static const uint32_t SPIKE_INTERVAL_USEC = 200;

static const float FREQ_MIN_HZ = 1000;
static const float FREQ_MAX_HZ = 10'000;

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

    printf("%d Hz => %lu\n", (int)freq_hz, spike_interval_usec);

    digitalWrite(OUTPUT_PIN, HIGH);
    delayMicroseconds(SPIKE_DURATION_USEC);
    digitalWrite(OUTPUT_PIN, LOW);

    delayMicroseconds(SPIKE_INTERVAL_USEC);
}
