/*
sensor-blink
This program blinks an LED after an IR proximity sensor triggers an input pin.
OP = optomized - remove unoptimized when finished
*/

// constants won't change:
const long interval = 1000;           // interval at which to blink (milliseconds)
const int maxPins = 15;                // 

// variables that change
int LEDStates[maxPins+1];
int sensorStates[maxPins+1];
int triggerStates[maxPins+1];
unsigned long onMillisMulti[maxPins+1];

void setup() {
  // set the digital pins as input/output:

  //OP

  for (int i = 0; i <= maxPins; i = i + 1)
  {
    LEDStates[i] = HIGH;
    sensorStates[i] = HIGH;
    triggerStates[i] = HIGH;
    onMillisMulti[i] = 0;
    pinMode(i + 16, OUTPUT);
    pinMode(i, INPUT);
    digitalWrite(i + 16, LEDStates[i]); // turn off LED
  }
  
  // setup serial port
  Serial.begin(9600);
  
}

void loop() 
{

  unsigned long currentMillis = millis();

 
  //OP block
  //int i;
  for (int i = 0; i <= maxPins; i++)  //use i not just as counter but as pin value as well, for LED Pin, add 16
  {
    if (triggerStates[i] == HIGH) //if not triggered, using i as the pin number
    {  
      sensorStates[i] = digitalRead(i);
      if (sensorStates[i] == LOW) // triggered
      {
        triggerStates[i] = LOW; //LOW = LED ON
        if (i<10)
        {
        Serial.print("0");
        Serial.print(i);
        }
        else
        {
        Serial.print(i); 
        }
        Serial.print("o");
      }
    }
    else
    {
      if (LEDStates[i] == HIGH) //LED off
      {
        LEDStates[i] = LOW; //set LED state to ON
        digitalWrite(i + 16, LEDStates[i]);
        onMillisMulti[i] = currentMillis;
      }
      if (currentMillis - onMillisMulti[i] >= interval)
      {
        //LED has been on long enough, turn it off
        LEDStates[i] = HIGH;
        triggerStates[i] = HIGH;
        digitalWrite(i + 16, LEDStates[i]);
        if (i<10)
        {
        Serial.print("0");
        Serial.print(i);
        }
        else
        {
        Serial.print(i); 
        }
        Serial.print("f");
      }
    }
  }

}
