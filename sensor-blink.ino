/*

sensor-blink

This program blinks an LED after an IR proximity sensor triggers an input pin.

OP = optomized - remove unoptimized when finished

*/

//const int LEDPin =  LED_BUILTIN;// the number of the LED pin
const int LEDPin =  16;// the number of the LED pin
const int sensorPin =  0;// the number of the LED pin
const int LEDPin2 =  17;// the number of the LED pin
const int sensorPin2 =  1;// the number of the LED pin

//OP
int LEDPins[] = {16,17,18}; //the pin number for the LEDs
int sensorPins[] = {0,1,2}; //the pin numbers for the sensors

// Variables will change:
int LEDState = HIGH;             // ledState used to set the LED (HIGH=off --- LOW=on)
int sensorState = HIGH;          // sensorState used to store state of IR sensor pin input  (HIGH = not triggered --- LOW = triggered)
unsigned long onMillis = 0;        // will store last time LED was updated
int triggerState = HIGH;       // triggerState used to store "triggered" state of IR sensor (even after IR sensor no longer triggered)
unsigned long onMillis2 = 0;        // will store last time LED was updated
int LEDState2 = HIGH;             // ledState used to set the LED (HIGH=off --- LOW=on)
int sensorState2 = HIGH;          // sensorState used to store state of IR sensor pin input  (HIGH = not triggered --- LOW = triggered)
int triggerState2 = HIGH;       // triggerState used to store "triggered" state of IR sensor (even after IR sensor no longer triggered)

//OP
int LEDStates[] = {HIGH, HIGH, HIGH};
int sensorStates[] = {HIGH, HIGH, HIGH};
int triggerStates[] = {HIGH, HIGH, HIGH};
unsigned long onMillisMulti[] = {0, 0, 0};

// constants won't change:
const long interval = 1000;           // interval at which to blink (milliseconds)

void setup() {
  // set the digital pins as input/output:
  pinMode(LEDPin, OUTPUT);
  pinMode(sensorPin, INPUT);
  pinMode(LEDPin2, OUTPUT);
  pinMode(sensorPin2, INPUT);

  //OP
  pinMode(LEDPins[0], OUTPUT);
  pinMode(LEDPins[1], OUTPUT);
  pinMode(LEDPins[2], OUTPUT);
  pinMode(sensorPins[0], INPUT);
  pinMode(sensorPins[1], INPUT);
  pinMode(sensorPins[2], INPUT);
  
  // turn off LED
  digitalWrite(LEDPin, LEDState);
  digitalWrite(LEDPin2, LEDState2);

  //OP
  digitalWrite(LEDPins[0], LEDStates[0]);
  digitalWrite(LEDPins[1], LEDStates[1]);
  digitalWrite(LEDPins[1], LEDStates[1]);

  // setup serial port
  Serial.begin(9600);
  
}

void loop() 
{

  unsigned long currentMillis = millis();


  if (triggerState == HIGH)   // if not triggered
  {

    // read the IR sensor pin to see if triggered
    int sensorState = digitalRead(sensorPin);

    if (sensorState == LOW)   // triggered
    {
       triggerState = LOW;    // LOW = LED ON!
       Serial.print("1");
    }
  }
  else
  {
    if (LEDState == HIGH)   // LED off
    {
      LEDState = LOW;   // set LED state to ON
      digitalWrite(LEDPin, LEDState);    
      onMillis = currentMillis;
    }
    
    if (currentMillis - onMillis >= interval) 
    {
      // LED has been on long enough -- turn it off
      LEDState = HIGH;
      triggerState = HIGH;
      digitalWrite(LEDPin, LEDState);
      //Serial.println("LED 1 OFF");
    }
  }

//same block, but for trig/sense 2
  if (triggerState2 == HIGH)   // if not triggered
  {

    // read the IR sensor pin to see if triggered
    int sensorState2 = digitalRead(sensorPin2);

    if (sensorState2 == LOW)   // triggered
    {
       triggerState2 = LOW;    // LOW = LED ON!
       Serial.print("2");
    }
  }
  else
  {
    if (LEDState2 == HIGH)   // LED off
    {
      LEDState2 = LOW;   // set LED state to ON
      digitalWrite(LEDPin2, LEDState2);    
      onMillis2 = currentMillis;
    }
    
    if (currentMillis - onMillis2 >= interval) 
    {
      // LED has been on long enough -- turn it off
      LEDState2 = HIGH;
      triggerState2 = HIGH;
      digitalWrite(LEDPin2, LEDState2);
      //Serial.println("LED 2 OFF");
    }
  }

 /*
  //OP block
  for (int i = 0; i < 16; i = i + 1 ) //use i not just as counter but as pin value as well, for LED Pin, add 16
  {
    if (triggerStates[i] == HIGH) //if not triggered, using i as the pin number
    {  
      sensorStates[i] = digitalRead(sensorPins[i]);

      if (sensorStates[i] == LOW) // triggered
      {
        triggerStates[i] = LOW; //LOW = LED ON
        Serial.print(i);
      }
    }
    else
    {
      if (LEDStates[i] == HIGH) //LED off
      {
        LEDStates[i] = LOW; //set LED state to ON
        digitalWrite(LEDPins[i], LEDStates[i]);
        onMillisMulti[i] = currentMillis;
      }
      if (currentMillis - onMillisMulti[i] >= interval)
      {
        //LED has been on long enough, turn it off
        LEDStates[i] = HIGH;
        triggerStates[i] = HIGH;
        digitalWrite(LEDPins[i], LEDStates[i]);
      }
    }
  }
*/  
}
