#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(10000);
  float humidity = dht.readHumidity();
  float temp = dht.readTemperature();

  String response = "{\"humidity\": " + String(humidity, 2) + ", \"temperature\": " + String(temp, 2) + "}";

  Serial.println(response);
}
