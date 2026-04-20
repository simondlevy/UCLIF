static const uint8_t PWM_PIN = 9;  // PWM output pin

static const uint8_t POT_PIN = A0; // Potentiometer for frequency control

static const uint32_t SPIKE_DURATION_USEC = 500;

static void sendSpike()
{
    digitalWrite(PWM_PIN, HIGH);
    delayMicroseconds(SPIKE_DURATION_USEC);
    digitalWrite(PWM_PIN, LOW);
}

void setup()
{
    Serial.begin(115200);

    pinMode(PWM_PIN, OUTPUT);
}

void loop()
{ 
    //const auto potValue = analogRead(POT_PIN);

    //const int delayTime = map(potValue, 0, 1023, 1000, 50);

    //const float FREQ_HZ = 2000;

    delayMicroseconds(100'000);

    sendSpike();

}
