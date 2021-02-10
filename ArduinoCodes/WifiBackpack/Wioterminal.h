#ifndef Wioterminal_h
#define Wioterminal_h

#include "Arduino.h"
#include <rpcWiFi.h>
#include <HTTPClient.h>


#include"TFT_eSPI.h"
#include "RTC_SAMD51.h"

#include <Arduino_JSON.h>

#define LCD_BACKLIGHT (72Ul) // Control Pin of LCD

class Wioterminal
{
  public:
    Wioterminal(int baudrate);
    void start();
    void checkwifi();
    void connectwifi();
    void tft_setup();
    void lookout1();
    void lookout();
    void decode_message(String request);



    private:
    String request;
    String _ret;
    int _baudrate;
    String _wifi;
    const char *host;
    int _port;
    char *_cport;
    int slash[3];
    int colon;
    const char *_url;
    char _proto[10];
    char _host[100];
    char _path[100];
    String line;
    
      //to store airtable credentials
      String appKey="";
      String BaseId="";


      //for airtable values
      String Field;
      String Value;
      String data;
      
  unsigned long timeout;
  uint32_t taketime;

};

#endif
