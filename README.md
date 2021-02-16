# ME35_21
This has the LabVIEW (and example) code for Robotics class in 2021.
To use this you will need to install Python3 on your machine and a few libraries
  1. pip3 install pyserial
  
There are a few useful things in this code:
  1. LabVIEW code that can save and read files on SPIKE Prime
  2. A REPL for SPIKE Prime to test out code (or save it)
  3. example code on SPIKE (under Browser)
  4. Milan's protocol for the WIO Terminal
  5. Browse files on SPIKE (Browser)
  6. Plot data coming over the console (Explorer)
  7. Save console log files for post-processsing

FAQ:
  1. Where do I get LabVIEW? It is free here - https://www.ni.com/en-us/support/downloads/software-products/download.labview-community.html#370001
  2. I am on Big Sur and LabVIEW is not working - open the Terminal and copy paste each of these commands (and hit return each time) - you only have to do this once - but that will let LabVIEW work on your machine
       <br>- <em>defaults write com.ni.labview NSGraphicsContextAllowOverRestore -bool YES</em>
       <br>- <em>defaults write com.ni.labview NSViewAllowsRootLayerBacking 0</em>
