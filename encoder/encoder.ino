static const uint8_t INPUT_PIN = A9;
static const uint8_t OUTPUT_PIN = 0;

static const uint32_t SPIKE_DURATION_USEC = 50;
static const uint32_t SPIKE_INTERVAL_USEC = 200;

void setup()
{
    pinMode(OUTPUT_PIN, OUTPUT);
}

void loop()
{ 
    const uint16_t input = 1023 - analogRead(INPUT_PIN);

    printf("%d\n", input);

    digitalWrite(OUTPUT_PIN, HIGH);
    delayMicroseconds(SPIKE_DURATION_USEC);
    digitalWrite(OUTPUT_PIN, LOW);

    delayMicroseconds(SPIKE_INTERVAL_USEC);
}
