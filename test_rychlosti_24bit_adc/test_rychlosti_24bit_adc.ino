//test rychlosti vzorkovania  HX711 24bit ADC
#include "HX711_lib.h"
int DT = A0;
int SCLK = A1;

//988300 bez vahy
//1203600 s 1000g
//215300 = 1000g -> 215 = 1g

//100 bits one message
//1000 bits 10 sensors
//hx711 conversion 0.1s



void setup() {
  Serial.begin(115200);
  pinMode(DT,INPUT);
  pinMode(SCLK,OUTPUT);
  digitalWrite(SCLK, LOW);
}

void loop() {
  if(digitalRead(DT) == 0)
  {
      delayMicroseconds(1);
      Serial.println(Get24bits(SCLK,DT));
  }
}
