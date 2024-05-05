#include <Arduino.h>
volatile float tiempo0 = 0;
volatile float tiempo1 = 0;

int RPM = 0;
float VEL = 0.00;
float VELMAX = 0.00;
float omega = 0;
const float pi = 3.14159;
const float dosPi = 6.28318;
const float radioIman = 0.12;    //En principio no hace falta para calcular la velocidad angular
const float radioRueda = 0.14;   //hace falta para calcular la velocidad lineal del coche
const int hallPin = 2;
const int ledRojo = 9;
const int ledVerde = 10;


void pulsoRueda(){
  
  tiempo1 = micros();
  omega = (dosPi*1000000 / (tiempo1 - tiempo0)); //Omega en radianes/segundo
  RPM = ((omega * 60) / dosPi);
  VEL = omega * radioRueda *3.6;   //Velocidad en Km/hora
  tiempo0 = tiempo1;
 

 Serial.print(RPM);
 Serial.print("RPM");
 Serial.print(VEL);
 Serial.print("    ");
 Serial.println(digitalRead(hallPin));
 
   
    
}

void setup(){
  pinMode(hallPin, INPUT);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  
  //Inicializacion del sistema
  digitalWrite(ledRojo, HIGH);
  digitalWrite(ledVerde, LOW);
  Serial.begin(9600);
  //inicializamos el texto en la pantalla
  digitalWrite(ledVerde, HIGH);
  digitalWrite(ledRojo, LOW);
  //Declaramos la interrupcion. En el arduino Micro (similar al leonardo). En el pin 1 se encuentra la interrupcion 3
  //Como tenemos una resistencia de PULL-UP nos interesa ejecutar el codigo cuando pasa de 5V a 0V --> FALLING
  attachInterrupt(1, pulsoRueda, FALLING);
}


void loop(){
  //baja la velocidad de escritura de la pantalla LCD
  delay(350);
  
  // Serial.println(VEL,2);
  if (VEL >= VELMAX){
    VELMAX = VEL;
  }else{
  }
}
