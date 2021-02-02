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