#include "ESP32Servo.h"

Servo servo;






void setup() 

{
  servo.attach(2);

  Serial.begin(115200);
}

void loop() 
{
  servo.write(0);
  delay(1000);
  servo.write(45);

  delay(1000);


}