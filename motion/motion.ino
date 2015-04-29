#include <State.h>
#include <SM.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)
#define BACKVERTICALBOTTOM 0
#define BACKVERTICALTOP 1
#define BACKHORIZONTAL 14
#define LEFTVERTICALBOTTOM 8
#define LEFTVERTICALTOP 9
#define LEFTHORIZONTAL 10
#define RIGHTVERTICALBOTTOM 11
#define RIGHTVERTICALTOP 12
#define RIGHTHORIZONTAL 13
#define N (3)
 
int CurrentState[N][N];
int GoalState[N][N];

//initial position
int LeftVerticalBottom = 450;
int LeftVerticalTop = 400;
int LeftHorizontal = 350;
int RightVerticalBottom = 350; 
int RightVerticalTop = 350;
int RightHorizontal = 350;
int BackVerticalBottom = 300;
int BackVerticalTop = 350;
int BackHorizontal = 400;

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);
  CurrentState[0][0] = LeftVerticalBottom;
  CurrentState[0][1] = LeftVerticalTop;
  CurrentState[0][2] = LeftHorizontal;
  CurrentState[1][0] = RightVerticalBottom;
  CurrentState[1][1] = RightVerticalTop;
  CurrentState[1][2] = RightHorizontal;
  CurrentState[2][0] = BackVerticalBottom;
  CurrentState[2][1] = BackVerticalTop;
  CurrentState[2][2] = BackHorizontal;
}

void loop() {
  String content = "";
  if (Serial.available()) {
    while (Serial.available()) {
      content += Serial.read();
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      int index = content.indexOf(","); //We find the next comma
      GoalState[i][j] = atol(content.substring(0,index).c_str()); //Extract the number
      content = content.substring(index+1); //Remove the number from the string
    }
  }
}
  
//  pwm.setPWM(0, 0, BackVerticalBottom);
//  pwm.setPWM(1, 0, BackVerticalTop);
//  pwm.setPWM(14, 0, BackHorizontal);
//  pwm.setPWM(8, 0, LeftVerticalBottom);
//  pwm.setPWM(9, 0, LeftVerticalTop);
//  pwm.setPWM(10, 0, LeftHorizontal);
//  pwm.setPWM(11, 0, RightVerticalBottom);
//  pwm.setPWM(12, 0, RightVerticalTop);
//  pwm.setPWM(13, 0, RightHorizontal);
//  if (Serial.available() > 0) {
//    int command = Serial.read();
//    
//    switch (command - 48) { //this was fun
//    case BACKVERTICALBOTTOM:
//      BackVerticalBottom = BackVerticalBottom + 10;
//      pwm.setPWM(0, 0, BackVerticalBottom);
//      break;
//    case BACKVERTICALTOP:
//      BackVerticalTop = BackVerticalTop + 10;
//      pwm.setPWM(1, 0, BackVerticalTop);
//      break;
//    case BACKHORIZONTAL:
//      BackHorizontal = BackHorizontal + 10;
//      pwm.setPWM(14, 0, BackHorizontal);
//      break;
//    case LEFTVERTICALBOTTOM:
//      LeftVerticalBottom = LeftVerticalBottom + 10;
//      pwm.setPWM(8, 0, LeftVerticalBottom);
//      break;
//    case LEFTVERTICALTOP:
//      LeftVerticalTop = LeftVerticalTop + 10;
//      pwm.setPWM(9, 0, LeftVerticalTop);
//      break;
//    case LEFTHORIZONTAL:
//      LeftHorizontal = LeftHorizontal + 10;
//      pwm.setPWM(10, 0, LeftHorizontal);
//      break;
//    case RIGHTVERTICALBOTTOM:
//      RightVerticalBottom = RightVerticalBottom + 10;
//      pwm.setPWM(11, 0, RightVerticalBottom);
//      break;
//    case RIGHTVERTICALTOP:
//      RightVerticalTop = RightVerticalTop + 10;
//      pwm.setPWM(12, 0, RightVerticalTop);
//      break;
//    case RIGHTHORIZONTAL:
//      RightHorizontal = RightHorizontal + 10;
//      pwm.setPWM(13, 0, RightHorizontal);
//      break;
//    default: 
//      Serial.println("Only 0-15 are supported.");
//    }
//    Serial.println(command);           // to the serial monitor
//  }
