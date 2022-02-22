#include"TFT_eSPI.h"

TFT_eSPI tft;
#define LCD_BACKLIGHT (72Ul) // Control Pin of LCD
String line = "";
int xdata[] = {0,2,3,4,10}; int ydata[] = {0,4,6,8,10}; int xmin = 0; int xmax = 10; int ymin = 0; int ymax = 10;
int screen = 0;

void TestLine() {
  int w = 100; int h = 100; int x0 = 10; int y0 = 10;int off = 5; int header = 12;
  line = "1(0)\n";  // clear screen
  line += "4(2,"+String(x0)+","+String(y0)+","+ String(w)+","+String(h)+",63000)\n"; //background
  line += "4(0,"+String(x0+off)+","+String(y0+h- 2*off)+","+ String(x0+w-off)+","+String(y0+h-2*off)+",10)\n"; //X axis
  line += "4(0,"+String(x0+2*off)+","+String(y0+h-off)+","+ String(x0+2*off)+","+String(y0+off+header)+",10)\n"; //Y axis
  for(int i = 1; i < 5;i++){
    int x1 = x0 + 2*off + float(xdata[i-1]-xmin)/(xmax-xmin)*(w-3*off);
    int x2 = x0 + 2*off + float(xdata[i]-xmin)/(xmax-xmin)*(w-3*off);
    int y1 = y0 + h - 2*off - float(ydata[i-1]-ymin)/(ymax-ymin)*(h-3*off-header);
    int y2 = y0 + h - 2*off - float(ydata[i]-ymin)/(ymax-ymin)*(h-3*off-header);
    line += "4(0,"+String(x1)+","+String(y1)+","+ String(x2)+","+String(y2)+",31)\n"; //plot
  }
 line += "2(10 kW,"+String(1)+","+String(x0+off)+","+ String(y0 + off)+",10)\n"; //Y Axis label
}

void setup() {
    pinMode(WIO_KEY_A, INPUT_PULLUP);
    pinMode(WIO_KEY_B, INPUT_PULLUP);
    pinMode(WIO_KEY_C, INPUT_PULLUP);  
    pinMode(WIO_5S_UP, INPUT_PULLUP);
    pinMode(WIO_5S_DOWN, INPUT_PULLUP);
    pinMode(WIO_5S_LEFT, INPUT_PULLUP);
    pinMode(WIO_5S_RIGHT, INPUT_PULLUP);
    pinMode(WIO_5S_PRESS, INPUT_PULLUP);
    Serial.begin(115200);
    Serial1.begin(115200);
    delay(1000);
    tft_setup();
//    if you want to run the test plot - TestLine(); show_Data();
}

void loop() {
  unsigned long startTime = millis();
  if (get_Data()) {
    String reply = show_Data();
    WaitAndCheckBtn(startTime);    // wait for the rest of the second to look for a button push
    Serial1.println(reply);
  }
  else WaitAndCheckBtn(startTime);
}

void WaitAndCheckBtn(unsigned long startTime){
  while ((millis() - startTime) < 1000) {
     if (digitalRead(WIO_5S_RIGHT) == LOW) {
      screen = (screen+1)%2;
      while (digitalRead(WIO_5S_RIGHT) == LOW) delay(100);
      break;
     }
     if (digitalRead(WIO_5S_LEFT) == LOW) {
      screen = (screen>0)?screen-1:0;
      while (digitalRead(WIO_5S_LEFT) == LOW) delay(100);
      break;
     }
     if (digitalRead(WIO_KEY_C) == LOW) {
        digitalWrite(LCD_BACKLIGHT, !digitalRead(LCD_BACKLIGHT));
        while (digitalRead(WIO_KEY_C) == LOW) delay(100);
     }
     if (digitalRead(WIO_KEY_A) == LOW) {
        Flicker();
        while (digitalRead(WIO_KEY_A) == LOW) delay(100);
        break;
     }
     delay(100);
  }
}

bool get_Data(){
    line = "";
    //Serial.setTimeout() = 1000;
    while (Serial1.available()) {
      line+=Serial1.readString();
      delay(1);
    }
    return line.length() > 0;
}

String show_Data(){
  Serial.println("parsing Data");
  Serial.println(line);
  //line = line.substring(line.indexOf("data:\n") + 6,line.length());
  return ParseLine(line);
}

String ParseLine(String line){
  Serial.println(line);
  int last = 0;
  String reply = "";
  Serial.println(line.indexOf("\n"));
  while ((last = line.indexOf("\n")) >= 0)  {
    String row = line.substring(0,last);
    line = line.substring(last+1,line.length());
    Serial.println(line);
    reply += Parse(row);
  }
 return reply;
}

String Parse(String row) {
  String reply ="";
  int cmd = row.substring(0,row.indexOf("(")).toInt();
  Serial.println("cmd = "+ String(cmd));
  switch (cmd) {
    
    case 0: { // delay(msec)  or  0(100)
      delay(FirstNum(row));
      return reply;
    }
    case 1: { // screen color  screen(color)  or  1(2016)
      tft.fillScreen(FirstNum(row));
      return reply;
    }     
    case 2: {// text     text(string,font,x,y,color) or 2(Hi "there &, 1,10,15, 2016)
      String message = NextStr(row,1);
      tft.setTextSize(NextStr(row,2).toInt());
      int x = NextStr(row,3).toInt();
      int y = NextStr(row,4).toInt();
      tft.setTextColor(LastNum(row));
      tft.drawString(message,x,y);
      return reply;
    }
    case 3: {// line     line(x0,y0,x1,y1,color) or 3(10,100, 100,100,2016)
      int x0 = NextStr(row,1).toInt();
      int y0 = NextStr(row,2).toInt();
      int x1 = NextStr(row,3).toInt();
      int y1 = NextStr(row,4).toInt();
      int color = LastNum(row);
      tft.drawLine(x0,y0,x1,y1,color);
      return reply;
     }
    case 4: {// shape     shape(type,x0,y0,x1,y1,color) or 4(1,10,100, 100,100,2016)
      Shape(row);
      return reply;
    }
  }
}

String NextStr(String row, int number){
  int loc = 2; String token = ",";
  for (int i=0;i<(number - 1);i++) loc = 1 + row.indexOf(token,loc);
  String reply = row.substring(loc,row.indexOf(token,loc));
  return reply;
}

int FirstNum(String row){
  String reply = row.substring(row.indexOf("(") + 1,row.length());
  return reply.toInt();
}

int LastNum(String row){
  String reply = row.substring(row.lastIndexOf(",") + 1,row.lastIndexOf(")"));
  return reply.toInt();
}

void Shape(String row) {
  int type = NextStr(row,1).toInt();
  int x0 = NextStr(row,2).toInt();
  int y0 = NextStr(row,3).toInt();
  int color = LastNum(row);
  switch (type) {
    case 0: {  // line
      int x1 = NextStr(row,4).toInt();  int y1 = NextStr(row,5).toInt();
      tft.drawLine(x0,y0,x1,y1,color);
      break;
    }
    case 1: {  // rectangle boundary
      int w = NextStr(row,4).toInt();  int h = NextStr(row,5).toInt();
      tft.drawRect(x0,y0,w,h,color);  
      break;
    }
    case 2: {  // filled rectangle 
      int w = NextStr(row,4).toInt();  int h = NextStr(row,5).toInt();
      tft.fillRect(x0,y0,w,h,color);  
      break;
    }
    case 3: {  // circle boundary
      int r = NextStr(row,4).toInt();
      tft.drawCircle(x0,y0,r,color);  
      break;
    }
    case 4: {  // filled circle 
      int r = NextStr(row,4).toInt();
      tft.fillCircle(x0,y0,r,color);  
      break;
    }
    case 5: {  // ellipse boundary
      int r1 = NextStr(row,4).toInt();  int r2 = NextStr(row,5).toInt();
      tft.drawEllipse(x0,y0,r1,r2,color); 
      break; 
    }
    case 6: {  // ellipse rectangle 
      int r1 = NextStr(row,4).toInt();  int r2 = NextStr(row,5).toInt();
      tft.fillEllipse(x0,y0,r1,r2,color);  
      break;
    }
    case 7: {  // triangle boundary
      int x1 = NextStr(row,4).toInt();  int y1 = NextStr(row,5).toInt();  int x2 = NextStr(row,6).toInt();  int y2 = NextStr(row,7).toInt();
      tft.drawTriangle(x0,y0,x1,y1,x2,y2,color);  
      break;
    }
    case 8: {  // filled triangle 
      int x1 = NextStr(row,4).toInt();  int y1 = NextStr(row,5).toInt();  int x2 = NextStr(row,6).toInt();  int y2 = NextStr(row,7).toInt();
      tft.fillTriangle(x0,y0,x1,y1,x2,y2,color);  
      break;
    }
    case 9: {  // rectangle boundary
      int w = NextStr(row,4).toInt();  int h = NextStr(row,5).toInt();  int r = NextStr(row,6).toInt();
      tft.drawRoundRect(x0,y0,w,h,r,color);  
      break;
    }
    case 10: {  // filled rectangle 
      int w = NextStr(row,4).toInt();  int h = NextStr(row,5).toInt();  int r = NextStr(row,6).toInt();
      tft.fillRoundRect(x0,y0,w,h,r,color);  
      break;
    }
  }
}

void tft_setup(){
  tft.begin();
  tft.setRotation(3);
  tft.fillScreen(TFT_GREEN);
  delay(1000);
  Flicker();
  tft.setTextSize(1);
}

void Flicker() {
  digitalWrite(LCD_BACKLIGHT, LOW);    // Turning off the LCD backlight
  delay(1000);
  digitalWrite(LCD_BACKLIGHT, HIGH);    // Turning on the LCD backlight
}