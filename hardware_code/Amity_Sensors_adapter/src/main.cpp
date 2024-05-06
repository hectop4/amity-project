#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085.h>
#include <DHT.h>
#include <DHT_U.h>
#include <SPI.h>

#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

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
  Serial.print(F("T:"));
  Serial.print(bmp.readTemperature());

  Serial.print(F("P:"));
  Serial.print(bmp.readPressure());


  Serial.print(F("H:"));
  Serial.print(bmp.readAltitude());


  Serial.print(F("Hu:"));
  Serial.print(dht.readHumidity());


  Serial.print(F("T2:"));
  Serial.println(dht.readTemperature());


  delay(2000);
}