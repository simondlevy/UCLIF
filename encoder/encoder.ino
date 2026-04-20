/* Simple Function Generator with Arduino Outputs: Square, Triangle, and Sine
 * (approximation) Frequency adjustable via potentiometer Waveform selection
 * via push button */
#define PWM_PIN 9 // PWM output pin
#define POT_PIN A0 // Potentiometer for frequency control
#define BTN_PIN 2 // Button for waveform selection

// Waveform types
enum Waveform {SQUARE, TRIANGLE, SINE};

Waveform currentWave = SQUARE;

unsigned long lastDebounce = 0;
const unsigned long debounceDelay = 200; // ms

// Sine wave lookup table (0-255 values for PWM)
const uint8_t sineTable[64] = { 128,140,153,165,177,188,198,207,
    215,222,227,231,234,235,235,234, 231,227,222,215,207,198,188,177,
    165,153,140,128,115,102, 90, 78, 67, 57, 48, 40, 33, 28, 24, 21, 20, 20,
    21, 24, 28, 33, 40, 48, 57, 67, 78, 90,102,115 };

void setup()
{
    pinMode(PWM_PIN, OUTPUT);
    pinMode(BTN_PIN, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop()

{ // Read potentiometer for frequency control
    
    int potValue = analogRead(POT_PIN);
    int delayTime = map(potValue, 0, 1023, 1000, 50);

    // Lower = faster // Check button press for waveform change
    if (digitalRead(BTN_PIN) == LOW && (millis() - lastDebounce) > debounceDelay) {
        lastDebounce = millis();
        currentWave = (Waveform)((currentWave + 1) % 3);

        Serial.print("Waveform changed to: ");

        if (currentWave == SQUARE) Serial.println("Square");

        else if (currentWave == TRIANGLE) Serial.println("Triangle");

        else Serial.println("Sine");

    }
    // Generate selected waveform
    switch (currentWave) {
        case SQUARE: analogWrite(PWM_PIN, 255);
                     delayMicroseconds(delayTime);
                     analogWrite(PWM_PIN, 0);
                     delayMicroseconds(delayTime);
                     break;

        case TRIANGLE: for (int i = 0;
                               i < 256;
                               i++) { analogWrite(PWM_PIN, i);
                           delayMicroseconds(delayTime);
                       } for (int i = 255;
                               i >= 0;
                               i--) { analogWrite(PWM_PIN, i);
                           delayMicroseconds(delayTime);
                       } break;
        case SINE: for (int i = 0;
                           i < 64;
                           i++) { analogWrite(PWM_PIN, sineTable[i]);
                       delayMicroseconds(delayTime);
                   } break;
    } 
}
