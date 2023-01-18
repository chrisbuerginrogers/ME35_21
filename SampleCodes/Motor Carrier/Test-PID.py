import time
from motorController import *

board = NanoMotorBoard()
print("reboot")
board.reboot()
time.sleep_ms(500)

#at 50 it works as expected, at 60 shift sides and is too small duty to move, at 70 is very big duty.
setDuty(0,0);
setDuty(0,1);
setDuty(0,2);
setDuty(0,3);

#Take the battery status
print('Battery Voltage: %d' % battery(1))
print('V Raw: %d' % battery(0))


  /************* PID 1 ***********************/

//  pid1.setControlMode(CL_POSITION);
//
//  //pid1.resetGains();
//  //pid1.setLimits(-100,100);
//  pid1.setGains(0.01f, 0.017f, 0.0f); //Proportional(change) Integral(change) Derivative
//  Serial.print("P Gain: ");
//  Serial.println((float)pid1.getPgain());
//  Serial.print("I Gain: ");
//  Serial.println((float)pid1.getIgain());
//  Serial.print("D Gain: ");
//  Serial.println((float)pid1.getDgain(), 7);
//  Serial.println("");
//
//  encoder1.resetCounter(0);
//  Serial.print("encoder1: ");
//  Serial.println(encoder1.getRawCount());
//  target = 1000;
//  pid1.setSetpoint(TARGET_POSITION, target);

  /************* PID 2 ***********************/

  pid2.setControlMode(CL_POSITION);

  //pid1.resetGains();
  //pid1.setLimits(-100,100);
  pid2.setGains(0.1f, 0.0f, 0.0f); //Proportional(change) Integral(change) Derivative
  Serial.print("P Gain: ");
  Serial.println((float)pid2.getPgain());
  Serial.print("I Gain: ");
  Serial.println((float)pid2.getIgain());
  Serial.print("D Gain: ");
  Serial.println((float)pid2.getDgain(), 7);
  Serial.println("");

  encoder2.resetCounter(0);
  Serial.print("encoder2: ");
  Serial.println(encoder2.getRawCount());
  target = 1000;
  pid2.setSetpoint(TARGET_POSITION, target);
  
while True:
    # ************* PID 1 ***********************/

    print("encoder1: %d" % encoder1.getRawCount())
//  Serial.print(" target: ");
//  Serial.println(target);
//  if (encoder1.getRawCount() == target) {
//    target += 1000;
//    Serial.print("Target reached: Setting new target..");
//    pid1.setSetpoint(TARGET_POSITION, target);
//    //delay(5000);
//  }

  /************* PID 2 ***********************/

  Serial.print("encoder2: ");
  Serial.print(encoder2.getRawCount());
  Serial.print(" target: ");
  Serial.println(target);
  if (encoder2.getRawCount() == target) {
    target += 1000;
    Serial.print("Target reached: Setting new target..");
    pid2.setSetpoint(TARGET_POSITION, target);
    //delay(5000);
  }

  //---------------------------------------
  controller.ping();
  //wait
  delay(50);
}
