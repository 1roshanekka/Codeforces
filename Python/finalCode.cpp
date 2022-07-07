// C++ code final
//
#include <Servo.h>

int moisture = 0;

int i = 0;

int position = 0;

int j = 0;

const int relayPin=13;
Servo servo_11;

void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(10000);
  pinMode(relayPin, OUTPUT);
  servo_11.attach(11, 500, 2500);

}

void loop()
{
  moisture = analogRead(A0);
  if (moisture > 500) {
    digitalWrite(relayPin,HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(8, LOW);
    digitalWrite(7, LOW);
    Serial.println("Low Moisture Level, Turning on pump");
    servo_11.write(45);
    delay(500); // Wait for 1000 millisecond(s)
    servo_11.write(0);
    delay(500); // Wait for 1000 millisecond(s)
  }
  else if (moisture < 200) {
	digitalWrite(relayPin,LOW);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
    digitalWrite(7, HIGH);
    Serial.println("Excellent Moisture Level, Pump is off");
  }else {
	digitalWrite(relayPin,LOW);
    digitalWrite(8, HIGH);
    digitalWrite(9, LOW);
    digitalWrite(7, LOW);
    Serial.println("Good Moisture Level, Pump is off");
  }
  
  //delay(10); // Delay a little bit to improve simulation performance
}