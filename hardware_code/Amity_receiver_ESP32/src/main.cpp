#include <Arduino.h>
#include <esp_now.h>
#include <WiFi.h>
#include <ESP32Servo.h>
#define led 2
//Motor Pins

#define in1 14
#define in2 27
#define in3 26
#define in4 25
#define in5 33
#define in6 32
#define in7 12
#define in8 13

//Stepper Pins
#define STEP 2
#define DIR 4

//Servo Pins
#define Servo1 5
#define Servo2 18

Servo servo1;
Servo servo2;

//Motor Functions

void forward(){
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);
  digitalWrite(in6, HIGH);
  digitalWrite(in7, LOW);
  digitalWrite(in8, LOW);
}

void backward(){
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
  digitalWrite(in5, LOW);
  digitalWrite(in6, LOW);
  digitalWrite(in7, HIGH);
  digitalWrite(in8, HIGH);
}

void left(){
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
  digitalWrite(in5, HIGH);
  digitalWrite(in6, HIGH);
  digitalWrite(in7, LOW);
  digitalWrite(in8, LOW);
}

void right(){
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, LOW);
  digitalWrite(in6, LOW);
  digitalWrite(in7, HIGH);
  digitalWrite(in8, HIGH);
}

void stop(){
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
  digitalWrite(in5, HIGH);
  digitalWrite(in6, HIGH);
  digitalWrite(in7, HIGH);
  digitalWrite(in8, HIGH);
}

typedef struct struct_message {
    char a[32];
} struct_message;

struct_message data;
// espnow function
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
   

  memcpy(&data, incomingData, sizeof(data));
  Serial.print("Bytes received: ");
  Serial.println(len);
  Serial.print("Char: ");
  Serial.println(data.a);

  switch (data.a[0])
  {
  case 'f':
    /* code */
    forward();
    break;
  case 'b':
    /* code */
    backward();
    break;
  case 'l':
    /* code */
    left();
    break;
  case 'r':
    /* code */
    right();
    break;
  case 's':
    /* code */
    stop();
    break;

  case 'c':
  servo1.write(0);
  servo2.write(0);
    break;
  case 'd':
  servo1.write(180);
  servo2.write(180);
    break;
  default:
  stop();
    break;
  }
  
  if(data.a[0]=='o'){
    digitalWrite(led, HIGH);
  }
  else{
    digitalWrite(led, LOW);
  }

   if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    stop();
    return;
  }

}

void setup() {

//Motor Pins
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);
  pinMode(in7, OUTPUT);
  pinMode(in8, OUTPUT);
  servo1.attach(Servo1);
  servo2.attach(Servo2);


  stop();

  // Initialize Serial Monitor
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  
  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    stop();
    return;
  }
  
  // Once ESPNow is successfully Init, we will register for recv CB to
  // get recv packer info
  esp_now_register_recv_cb(OnDataRecv);



}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    char c = Serial.read();
    Serial.println(c);
    switch (c)
    {
    case 'f':
      /* code */
      forward();
      break;
    case 'b':
      /* code */
      backward();
      break;
    case 'l':
      /* code */
      left();
      break;
    case 'r':
      /* code */
      right();
      break;
    case 's':
      /* code */
      stop();
      break;
    
    default:
    stop();
      break;
    }
  }
}
