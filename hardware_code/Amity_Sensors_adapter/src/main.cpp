#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085.h>
#include <DHT.h>
#include <DHT_U.h>
#include <SPI.h>
#include <string.h>

#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

String message="";

Adafruit_BMP085 bmp;

void setup() {
  Serial.begin(115200);
  Serial.println(F("BMP085 test"));

  if (!bmp.begin()) {
    Serial.println(F("Could not find a valid BMP085 sensor, check wiring!"));
    while (1) {}
  }

  dht.begin();
}

void loop() {

  //full message
  message = "T:" + String(bmp.readTemperature()) + ",P:" + String(bmp.readPressure()) + ",H:" + String(bmp.readAltitude()) + ",Hu:" + String(dht.readHumidity()) + ",T2:" + String(dht.readTemperature());
Serial.println(message);

  delay(100);
}