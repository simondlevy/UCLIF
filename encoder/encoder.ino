static const uint8_t PWM_PIN = 9;  // PWM output pin

static const uint32_t SPIKE_DURATION_USEC = 500;

const float FREQ_HZ = 40;

void setup()
{
    pinMode(PWM_PIN, OUTPUT);
}

void loop()
{ 
    // Delay for inter-spike interval
    delayMicroseconds(1'000'000 / FREQ_HZ);

    // Send spike
    digitalWrite(PWM_PIN, HIGH);
    delayMicroseconds(SPIKE_DURATION_USEC);
    digitalWrite(PWM_PIN, LOW);

}
