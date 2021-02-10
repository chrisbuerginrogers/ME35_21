#include "Wioterminal.h"
#include <rpcWiFi.h>
#include <WiFiClientSecure.h>
#include "TFT_eSPI.h"
#include "RTC_SAMD51.h"
#include <Arduino_JSON.h>
#include <HTTPClient.h>


#include <SPI.h>
//#include <Seeed_FS.h>
 

WiFiClientSecure client;
WiFiClient client1;

#define LCD_BACKLIGHT (72Ul) // Control Pin of LCD

TFT_eSPI tft;
DateTime now;
RTC_SAMD51 rtc;

int i =1;
String beginning="";
String ending="";
int prev_time, currenttime;
int func=0;

//to store wifi credentials
const char *_ssid;
const char *_password;


Wioterminal::Wioterminal(int baudrate) {
    _baudrate=baudrate;
}

void Wioterminal::start() {

  Serial.begin(115200);
  Serial1.begin(115200);
    rtc.begin();
    tft_setup();
 }

void Wioterminal::tft_setup(){
  tft.begin();
  tft.setRotation(3);
  tft.fillScreen(TFT_GREEN);

  delay(1000);
  // Turning off the LCD backlight
  digitalWrite(LCD_BACKLIGHT, LOW);
  delay(1000);
  // Turning on the LCD backlight
  digitalWrite(LCD_BACKLIGHT, HIGH);

  tft.setTextSize(1);
}


void Wioterminal::lookout(){

  if (Serial1.available()){
    prev_time=rtc.now().unixtime();
    do{
      beginning=Serial1.readString();
      ending+=beginning;
      }
    while(ending.indexOf("done")<0&&(rtc.now().unixtime()-prev_time)<2);   
    if(ending.indexOf("done")<0)
      {
        Serial1.write("False");
      }
    else {
         _ret=" ";
         request= String(ending);
         request=request.substring(0,request.length()-4);  //4 is to remove "done"
         Serial.println(request);
         decode_message(request);
         
         _ret=_ret+"True";
        Serial1.println(_ret);
      }
      ending="";
      Serial1.flush();
    }
}
void Wioterminal::decode_message(String request){
  String function;
  String lib;
  String arg;
  
  //request=request.substring(0,request.length()-4); //4 is to remove "done"
  JSONVar myObject = JSON.parse(request);
  func = atoi((const char*) myObject["function"]);
  lib=myObject["lib"];

  if(lib=="graphics"){

    switch (func){
      case 1: //"drawString"
      tft.drawString((const char*) myObject["arg"][0],atoi((const char*) myObject["arg"][1]),atoi((const char*) myObject["arg"][2]));
      _ret="True";
      break;
      
      case 2: //"fillScreen"
      tft.fillScreen(atoi((const char*) myObject["arg"][0]));
      _ret="True";
      break;
      
      case 3: //"setTextSize"
      tft.setTextSize(atoi((const char*) myObject["arg"][0]));
      _ret="True";
      break;
      
      case 4: //"drawLine"
      tft.drawLine(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]));
      _ret="True";    
      break;
      
     case 5: //"drawPixel"
     tft.drawPixel(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]));
     _ret="True";
     break;
      
     case 6: //"drawRect"
     tft.drawRect(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]));
     _ret="True";
     break;
     
     case 7: //"fillRect"
     tft.fillRect(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]));
     _ret="True";
     break;
        
     case 8: //"drawCircle"
     tft.drawCircle(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]));
     _ret="True";
     break;
         
     case 9: //"fillCircle"
     tft.fillCircle(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]));
     _ret="True";
     break;
        
     case 10: //"drawTriangle"
     tft.drawTriangle(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]), atoi((const char*) myObject["arg"][5]), atoi((const char*) myObject["arg"][6]));
     _ret="True";
     break;
       
     case 11: //"fillTriangle"
      tft.fillTriangle(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]), atoi((const char*) myObject["arg"][5]), atoi((const char*) myObject["arg"][6]));
      _ret="True";
      break;
       
     case 12: //"drawRoundRect"
     tft.drawRoundRect(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]), atoi((const char*) myObject["arg"][5]));
     _ret="True";
     break;
       
     case 13: //"fillRoundRect")
     tft.fillRoundRect(atoi((const char*) myObject["arg"][0]), atoi((const char*) myObject["arg"][1]), atoi((const char*) myObject["arg"][2]), atoi((const char*) myObject["arg"][3]), atoi((const char*) myObject["arg"][4]), atoi((const char*) myObject["arg"][5]));
     _ret="True";
     break;
  
      default: 
      break;
    }
  }

else if(lib=="wifi"){
  int m,n;
  colon=0;
  switch (func){
  case 1: //"Connect_wifi"
        _ssid=(const char*) myObject["arg"][0];
        _password=(const char*) myObject["arg"][1];
        WiFi.begin(_ssid,_password);
        while (WiFi.status() != WL_CONNECTED)
          {
          Serial.println(_ssid);
          Serial.println(_password);
          WiFi.begin(_ssid,_password);
           
        }
        Serial.println("Connected");
        _ret="Connected";
        break;
      
  case 2: //"general get"  work in progress
    line="";
     _url=(const char*) myObject["arg"][0];

     for(m=0,n=0;m<strlen(_url);m++){
        if(_url[m]==':' && n==2){
          colon=m;
        }
        if(_url[m]=='/'){
          slash[n]=m;
          n+=1;
          if(n==3){
            break;
          }
        }
      }

      (String(_url).substring(0,slash[0])).toCharArray(_proto,slash[0]); 
      if(colon == 0){
        (String(_url).substring(slash[1]+1,slash[2])).toCharArray(_host,slash[2]-slash[1]);
      }
      else{
        (String(_url).substring(slash[1]+1,colon)).toCharArray(_host,colon-slash[1]);
      }
      (String(_url).substring(slash[2])).toCharArray(_path,strlen(_url)-slash[2]+1);
     

      if(strcmp(_proto,"https")==0){
        _port=443;
        if (!client.connect(_host, _port))
          {
          Serial1.println("connection failed");
          tft.drawString("Connection failed",50,10);
          }
        client.println("GET " + String(_url) +" HTTP/1.1");
        client.println("Host: " + String(_host));
        
        client.println("Content-type: application/json");
        client.println("AppKey:....."); //sorry had to hide this
        client.println( "Connection: close");
        client.println();
        timeout = millis();
        while (client.available() == 0) {
          if (millis() - timeout > 5000) {
            _ret=">>> Client Timeout !";
            client.stop();
            break;
            }
          }
        taketime = millis();
        while (client.available())
          {
          line+= client.readStringUntil('\r');
          }
        _ret+=line;
        
        } 

        
      else if (strcmp(_proto,"http")==0){
        _port=80;
        if (!client1.connect(_host, _port))
          {
          Serial1.println("connection failed");
          tft.drawString("Connectio failed",50,10);
          }
        client1.println("GET " + String(_url) +" HTTP/1.0");
        client1.println("Host: " + String(_host));
        
        client1.println("Content-type: application/json");
        client1.println( "Connection: close");
        client1.println();
        timeout = millis();
        while (client1.available() == 0) {
          if (millis() - timeout > 5000) {
            _ret=">>> Client Timeout !";
            client1.stop();
            break;
            }
          }
        taketime = millis();
        while (client1.available())
          {
          line+= client1.readStringUntil('\r');
          }
        _ret+=line;
        
        }  
      else{
        _ret="Use http or https with your url";
        }
        break;


      case 3: //general put


      break;

      case 4: //set airtable
          appKey=(const char*) myObject["arg"][0];
          BaseId=(const char*) myObject["arg"][1];
          _ret="True";
          break;

      case 5: //get airtable
          if (!client.connect("api.airtable.com", 443)) {
              Serial.println("Connection failed!");
              delay(5000);
              return;
              } 
          Serial.println("Connected to server!");
          // Make a HTTP request:
          client.println("GET /v0/"+ BaseId +"/" + (const char*) myObject["arg"][0] +" HTTP/1.1");
          client.println("Host: api.airtable.com");
          client.println("Content-type:application/json"); 
          client.println("Accept: application/json"); 
          client.println("Authorization: Bearer " + appKey); 
          client.println("Connection: close");
          client.println();
          while (client.connected()) {
              line = client.readStringUntil('\n');
              if (line == "\r") {
                  Serial.println("headers received");
                  break;
                }
              }
          while (client.available()) {
            char c = client.read();
            if (c == '\n') {
                Serial.write('\r');
                }
              line+=c;
              }
          client.stop();
          _ret=line;
          Serial.println(_ret);
           break;


      case 6: //put airtable

        Field=String((const char*) myObject["arg"][1]);
        Value=String((const char*) myObject["arg"][2] );
        data= "{\"records\":[{\"fields\":{\""+Field+ "\":\"" +Value+"\"}}]}";
          if (!client.connect("api.airtable.com", 443)) {
              Serial.println("Connection failed!");
              delay(5000);
              return;
              } 
          Serial.println("Connected to server!");
            // Make a HTTP request:
          client.println("POST /v0/"+ BaseId +"/" + (const char*) myObject["arg"][0] +" HTTP/1.1");
          client.println("Host: api.airtable.com");
          client.println("Connection: keep-alive");
          client.println("Keep-Alive: timeout=10, max=100");
          client.println("Content-Type: application/json");
       
          client.print("Content-Length: ");
          client.println(data.length());
          client.println("Authorization: Bearer " + appKey);
          client.println("Accept: application/json");
      
          client.println();
          client.println(data);

          while (client.connected()) {
              line = client.readStringUntil('\n');
              if (line == "\r") {
                  Serial.println("headers received");
                  break;
                }
              }
          while (client.available()) {
            char c = client.read();
            if (c == '\n') {
                Serial.write('\r');
                }
              line+=c;
              }
          client.stop();
          _ret=line;
          Serial.println(_ret);
          break;
      
    default: 
      break;
    }
  }
}


void wifi_connect(){
    while(WiFi.status() != WL_CONNECTED)
        {
        Serial.println(_ssid);
        Serial.println(_password);
        WiFi.begin(_ssid,_password);  
        }
        Serial.println("Connected");
}
