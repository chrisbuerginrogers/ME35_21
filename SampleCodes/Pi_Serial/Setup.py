# upgrade everything
sudo apt update
sudo apt full-upgrade

# check and update pip
pip3 -V
#pip3 install --upgrade pip

# install opencv - https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=259426
sudo apt-get update
sudo apt-get install python3-opencv
sudo apt-get install libhdf5-dev
#sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test 

# install flask (probably already installed)
sudo apt-get install python3-flask

#try grabbing an image and make sure it saves it
raspistill -v -o test.jpg

