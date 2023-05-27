//----------------------------------------------------------
//sensor main v0 library read HX711 data
//----------------------------------------------------------

#include <Arduino.h>
#include "HX711_lib.h"

uint32_t Get24bits(int SCLK, int DT)
/*
  function read 25 bits 
*/
{
  digitalWrite(SCLK, LOW);
  uint32_t out = 0;
  for(int i = 24; i >= 0; i--)
  {
    digitalWrite(SCLK, HIGH);
    delayMicroseconds(1);
    out |= ((uint32_t)digitalRead(DT) << i);
    digitalWrite(SCLK, LOW);
    delayMicroseconds(1);
  }
  return out;
}
