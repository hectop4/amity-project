#include <esp_now.h>
#include <WiFi.h>

// REPLACE WITH YOUR RECEIVER MAC Address
uint8_t broadcastAddress[] = {0x94, 0xE6, 0x86, 0x3D, 0x82, 0xCC};
//94:E6:86:3D:82:CC

//This MAC is C8:C9:A3:D0:92:E4
// Define variables to store incoming readings
float incomingTemp;
float incomingHum;
float incomingPres;
// Structure example to send data
// Must match the receiver structure
typedef struct struct_message {
  char a[2];

} struct_message;

typedef struct struct_sens {
  float temp;
  float hum;
  float press;
  float alt;

} struct_sens;

// Create a struct_message called myData
struct_message myData;

struct_sens incomingReadings;

esp_now_peer_info_t peerInfo;

// callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&incomingReadings, incomingData, sizeof(incomingReadings));
  Serial.print("Bytes received: ");
  Serial.println(len);
  incomingTemp = incomingReadings.temp;
  incomingHum = incomingReadings.hum;
  incomingPres = incomingReadings.press;
}

void setup() {
  // Init Serial Monitor
  Serial.begin(115200);
 
  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  esp_now_register_send_cb(OnDataSent);
  
  // Register peer
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;
  
  // Add peer        
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }
  strcpy(myData.a, "");
}
 
void loop() {
  // Set values to send

  
  if(Serial.available()>0){
    char data = Serial.read();
    //Read all text and save it in a
    Serial.print(data);
    myData.a[0] = data;


  }
  
  // Send message via ESP-NOW
  esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));
   
  if (result == ESP_OK) {
    Serial.println("Sent with success");
  }
  else {
    Serial.println("Error sending the data");
  }
  delay(100);
}