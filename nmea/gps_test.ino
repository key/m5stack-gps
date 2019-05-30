//
// Tested M5Stack GPS module with M5Stack grey.
//
// Requirements:
// - MicroNMEA
//
// see: https://github.com/stevemarple/MicroNMEA
//
#include <M5Stack.h>
#include <MicroNMEA.h>

HardwareSerial gps(Serial2);

char buffer[85];
MicroNMEA nmea(buffer, sizeof(buffer));

float longitude, latitude, alt;
long altitude;

void setup() {
  M5.begin();

  Serial.begin(115200);
  gps.begin(9600);

  Serial.println("Setup done.");
}

void loop() {
  while (gps.available()) {
    M5.Lcd.setCursor(0, 0);
    M5.Lcd.setTextColor(WHITE, BLACK);
    M5.Lcd.setTextSize(3);
    M5.Lcd.printf("GPS available\r\n");

    char c = gps.read();

    if (nmea.process(c)) {
      char nav = nmea.getNavSystem();
      M5.Lcd.println(nav);

      if (nmea.isValid()) {
        longitude = nmea.getLongitude() / 1000000.0;
        latitude = nmea.getLatitude() / 1000000.0;
        nmea.getAltitude(altitude);
        alt = altitude / 1000.0;
        Serial.printf("longitude=%.6f, latitude=%.6f, altitude=%.6f\r\n", longitude, latitude, alt);

        M5.Lcd.setTextColor(GREEN, BLACK);
        M5.Lcd.printf("GPS: FIXED    \r\n");
        M5.Lcd.setTextColor(WHITE, BLACK);
        M5.Lcd.printf("Lng: %.6f\r\n", longitude);
        M5.Lcd.printf("Lat: %.6f\r\n", latitude);
        M5.Lcd.printf("Alt: %.2fm    \r\n", alt);
      } else {
        M5.Lcd.setTextColor(RED, BLACK);
        M5.Lcd.printf("GPS: NOT FIXED\r\n");
      }
    }
  }
}
