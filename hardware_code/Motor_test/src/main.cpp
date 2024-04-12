#include "BTS7960.h"

const uint8_t EN1 = 21;
const uint8_t L_PWM1= 19;
const uint8_t R_PWM1 = 18;

const uint8_t EN2 = 14;
const uint8_t L_PWM2 = 26;
const uint8_t R_PWM2 = 27;
BTS7960 motorController1(EN1, L_PWM1, R_PWM1);
BTS7960 motorController2(EN2, L_PWM2, R_PWM2);
int speed =125;
void setup() 
{
}

void loop() 
{
  motorController1.Enable();
  motorController2.Enable();


  motorController1.TurnLeft(speed);
  motorController2.TurnRight(speed);
  delay(1000);
  

  motorController1.Stop();
  motorController2.Stop();
  

  motorController1.TurnLeft(speed);
  motorController2.TurnRight(speed);
  delay(1000);
 
  motorController1.Stop();
  motorController2.Stop();
  motorController1.Disable();
  motorController2.Disable();
  delay(5000);

    motorController1.Enable();
  motorController2.Enable();


  motorController1.TurnRight(speed);
  motorController2.TurnLeft(speed);
  delay(1000);
  

  motorController1.Stop();
  motorController2.Stop();
  

  motorController1.TurnRight(speed);
  motorController2.TurnLeft(speed);
  delay(1000);
 
  motorController1.Stop();
  motorController2.Stop();
  motorController1.Disable();
  motorController2.Disable();
  delay(5000);
}