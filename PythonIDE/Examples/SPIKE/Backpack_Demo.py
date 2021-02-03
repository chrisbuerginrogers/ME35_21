import hub
import utime
import backpack

#ESTABLISHING CONNECTION - Very Important Step 
#connecting the WIO to port C - change C to whatever port you are using on SPIKE
t=backpack.screen(hub.port.C)


###########################
#colors are 16 bit integers
#pure blue is 31    - 00000 000000 11111
#pure green is 2016 - 00000 111111 00000
#pure red is 63488  - 11111 000000 00000 
# add the numbers to get the color of your choice

#so if you need yellow you should add red and green i.e. 65504 - 11111 111111 00000
#create your own colors 
# I have defined a couple for you to get started with
###########################
#Colors
BLUE=31
GREEN=2016
RED=63488
YELLOW=65504
VIOLET=63519
TEAL= 32896
WHITE=65535
BLACK=0
GRAY=50712


#filling the screen with color 65504
t.fillScreen(YELLOW)


#setTextSize to 3
t.setTextSize(3)
t.drawString("Size 3",200,50)

#setTextSize to 2
t.setTextSize(2)
t.drawString("Size 2",200,100)


#drawLine from (20,20) to (180,20) of color 31 i.e blue
t.drawLine(x1=20,y1=20,x2=180,y2=20,color=BLUE)


#drawPixel at 40,40 of color 65535 i.e. white
t.drawPixel(x=100,y=10,color=WHITE)

#drawRect from (20,30) with width 50 and height 50 of color GRAY
t.drawRect(x=20,y=30,h=50,w=50,color=GRAY)


#draw a filled rectangle from (130,30) with width 50 and height 50 with color RED
t.fillRect(x=130,y=30,h=50,w=50,color=RED)

#drawCircle with center at 100,40 with radius 20 of color WHITE
t.drawCircle(100,40,20,WHITE)

#draw a filled circle at center 100,80 with radius 20 with color BLACK
t.fillCircle(x=100,y=80,r=20,color=BLACK)

#drawTriangle with vertices at (30,40),(60,70), (30,70) 
t.drawTriangle(x1=30,y1=40,x2=60,y2=70,x3=30,y3=70,color=TEAL)

#fill a triangle at (170,40),(140,70),(170,70) with color WHITE
t.fillTriangle(x1=170,y1=40,x2=140,y2=70,x3=170,y3=70,color=WHITE)

#drawRoundRect with vertices at (20,100) with width 50 and height 50 and with a corner radius of 5 of color 63488
t.drawRoundRect(x=20,y=100,h=50,w=50,r=5,color=63488)

#fillRoundRect with vertices at (130,100) with width 50 and height 50 with corner radius of 5 with color GREEN
t.fillRoundRect(x=130,y=100,h=50,w=50,r=5,color=GREEN)

#CONNECTING TO WIFI

#connect to wifi with ssid ="ssid" and password="password"
t.connectWifi(ssid="ssid",pwd="password")

#WORKING WITH AIRTABLE

#set airtable with appkey="appkey" and baseID="baseid"
t.setAirtable(AppKey="appkey",baseID="baseid")

#post to airtable with table name="Table" and Field name="Variables" with value="ttt"
b=t.postAirtable(table="Table",field="Variables",value="ttt")

#get info of Airtable with Table name= "Table"
a=t.getAirtable(table="Table")

print(a)

