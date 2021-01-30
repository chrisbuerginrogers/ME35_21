import hub
import utime
import backpack
t=backpack.screen(hub.port.C)


##colors are 16 bit integers
#pure blue is 31
#pure green is 2016
#pure red is 63488
# add the numbers to get the color of your choice

#Here are some TFT commands - you can draw lines, rectangles, circles etc. look at wio's wiki or backpack.py for function names
t.drawString("STRING ",19,93)
t.fillScreen(431) #431 is the color 

# connect to your wifi
t.connectWifi("ssid","password")


#to use airtable api you should start by connecting to wifi, setting up airtable credentials and then call get or post 

t.setAirtable("airtable app key","airtable base ID") #you just need to do this once in the program

b=t.postAirtable("table_name","field_name","field_value") # make sure there are no spaces in the table name
a=t.getAirtable("table_name")

print(a)
