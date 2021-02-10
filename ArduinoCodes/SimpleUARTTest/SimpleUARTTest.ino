#include"TFT_eSPI.h"

TFT_eSPI tft;
#define LCD_BACKLIGHT (72Ul) // Control Pin of LCD
String line = "";

void setup() {

    Serial.begin(115200);
    Serial1.begin(9600);
    delay(1000);
    tft_setup();
}

void loop() {
  if (get_Data()) show_Data();
  Serial.print(".");
  delay(100);
}

bool get_Data(){
    line = "";
    while (Serial1.available()) {
      line+=Serial1.readString();
      delay(1);
    }
    return line.length() > 0;
}

void show_Data(){
  Serial.println("parsing Data");
  Serial.println(line);
  tft.drawString(line,10,50);
}

void tft_setup(){
  tft.begin();
  tft.setRotation(3);
  tft.fillScreen(TFT_GREEN);
  delay(1000);
  Flicker();
  tft.setTextSize(3);
}

void Flicker() {
  digitalWrite(LCD_BACKLIGHT, LOW);    // Turning off the LCD backlight
  delay(1000);
  digitalWrite(LCD_BACKLIGHT, HIGH);    // Turning on the LCD backlight
}
