#include <Adafruit_NeoPixel.h>
#include <Servo.h>

#define PIN 2	 // pin Neopixel is attached to
#define SENSOR A0		//input pin for Potentiometer
#define NUMPIXELS 1 // number of neopixels in strip

#define dryThreshold 50 //below this value, begin alerting dry, turn red;
#define wetThreshold 200 //above this value, begin alerting wet,turn blue;
#define thresholdCenter (dryThreshold + wetThreshold)/2 //Brightest Green point
#define crossFade 20 //how much blue and red should fade in to green


int moisture = 0;

int i = 0;

int position = 0;

int j = 0;

Servo servo_12;


Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int delayval = 100;

int redColor = 0;
int greenColor = 0;
int blueColor = 0;


int sensorValue  = 0;
int transitionValue = 0;


void setup() {
  // Initialize the NeoPixel library.
  pinMode(A0, INPUT);
  pixels.begin();
  pinMode(SENSOR,INPUT);
  servo_12.attach(12, 500, 2500);
}

void loop() {
	sensorValue = analogRead(SENSOR);
	transitionValue = map(sensorValue,0,1023,0,255);
	setColor();
    pixels.setPixelColor(0,redColor,greenColor,blueColor);
	
   
    pixels.show();
    moisture = analogRead(A0);
    if (moisture > 500) {
        servo_12.write(90);
    } else {
        servo_12.write(0);
    }
    //delay(10); // Delay a little bit to improve simulation performance
  
    delay(delayval); 
}

void setColor(){

  
  
redColor = ((transitionValue <= dryThreshold + crossFade) && (transitionValue >= 0 ))? map(transitionValue,0,dryThreshold + crossFade,255,0) : 0;
  
blueColor = (transitionValue >= wetThreshold - crossFade && transitionValue <= 255)? map(transitionValue,wetThreshold - crossFade,255,0,255):0; 
  
  
  if(transitionValue >= dryThreshold && transitionValue <= thresholdCenter)
  {
  greenColor = map(transitionValue,dryThreshold,thresholdCenter,0,255);
  }
  else if(transitionValue > thresholdCenter && transitionValue < wetThreshold)
  {
    greenColor = map(transitionValue,dryThreshold,thresholdCenter,255,0);
  }
  else{
    greenColor = 0;
  }
                   
}