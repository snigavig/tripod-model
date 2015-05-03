#include <State.h>
#include <SM.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)
#define RIGHTVERTICALBOTTOM 11
#define RIGHTVERTICALTOP 12
#define RIGHTHORIZONTAL 13
#define LEFTVERTICALBOTTOM 8
#define LEFTVERTICALTOP 9
#define LEFTHORIZONTAL 10
#define BACKVERTICALBOTTOM 0
#define BACKVERTICALTOP 1
#define BACKHORIZONTAL 14
#define N (3)
 
int CurrentState[N][N];
int GoalState[N][N];
int DifferenceBetweenStates[N][N];
int Stand1State[N][N];

//initial position
int RightVerticalBottom = 380; 
int RightVerticalTop = 400;
int RightHorizontal = 350;
int LeftVerticalBottom = 250;
int LeftVerticalTop = 350;
int LeftHorizontal = 350;
int BackVerticalBottom = 420;
int BackVerticalTop = 390;
int BackHorizontal = 400;

//jump position
//int RightVerticalBottom = 380; 
//int RightVerticalTop = 400;
//int RightHorizontal = 350;
//int LeftVerticalBottom = 400;
//int LeftVerticalTop = 350;
//int LeftHorizontal = 350;
//int BackVerticalBottom = 470;
//int BackVerticalTop = 480;
//int BackHorizontal = 400;

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);
  Stand1State[0][0] = RightVerticalBottom;
  Stand1State[0][1] = RightVerticalTop;
  Stand1State[0][2] = RightHorizontal;
  Stand1State[1][0] = LeftVerticalBottom;
  Stand1State[1][1] = LeftVerticalTop;
  Stand1State[1][2] = LeftHorizontal;
  Stand1State[2][0] = BackVerticalBottom;
  Stand1State[2][1] = BackVerticalTop;
  Stand1State[2][2] = BackHorizontal;
  move_to_stand_1();
  delay(500);
}

//////////////////////////// ~ M A I N ~ L O O P ~ ////////////////////////////
void loop() {
  String content = "";
  if (Serial.available()) {
    while (Serial.available()) {
      content += Serial.readString();
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        int index = content.indexOf(","); //We find the next comma
        GoalState[i][j] = atol(content.substring(0,index).c_str()); //Extract the number
        content = content.substring(index+1); //Remove the number from the string
      }
    }
    
    calculate_difference();
    move_to_goal_state();
  }
  
  Serial.println(current_state_to_string());
  
  delay(500);
}
//////////////////////////// ~ M A I N ~ L O O P ~ END ~ ////////////////////////////

String current_state_to_string() {
  String result;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      result += CurrentState[i][j];
      if (!(i==2 && j==2)) {
        result += ",";
      }
    }
  }
  return result;
}  

String goal_state_to_string() {
  String result;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      result += GoalState[i][j];
      if (!(i==2 && j==2)) {
        result += ",";
      }
    }
  }
  return result;
} 

void calculate_difference() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      DifferenceBetweenStates[i][j] = CurrentState[i][j] - GoalState[i][j];
    }
  }
}

void move_to_goal_state() {
  move_servo(RIGHTVERTICALBOTTOM, GoalState[0][0]);
  move_servo(RIGHTVERTICALTOP, GoalState[0][1]);
  move_servo(RIGHTHORIZONTAL, GoalState[0][2]);
  move_servo(LEFTVERTICALBOTTOM, GoalState[1][0]);
  move_servo(LEFTVERTICALTOP, GoalState[1][1]);
  move_servo(LEFTHORIZONTAL, GoalState[1][2]);
  move_servo(BACKVERTICALBOTTOM, GoalState[2][0]);
  move_servo(BACKVERTICALTOP, GoalState[2][1]);
  move_servo(BACKHORIZONTAL, GoalState[2][2]);
  CurrentState[0][0] = GoalState[0][0];
  CurrentState[0][1] = GoalState[0][1];
  CurrentState[0][2] = GoalState[0][2];
  CurrentState[1][0] = GoalState[1][0];
  CurrentState[1][1] = GoalState[1][1];
  CurrentState[1][2] = GoalState[1][2];
  CurrentState[2][0] = GoalState[2][0];
  CurrentState[2][1] = GoalState[2][1];
  CurrentState[2][2] = GoalState[2][2];
}

void move_to_stand_1() {
  move_servo(RIGHTVERTICALBOTTOM, Stand1State[0][0]);
  move_servo(RIGHTVERTICALTOP, Stand1State[0][1]);
  move_servo(RIGHTHORIZONTAL, Stand1State[0][2]);
  move_servo(LEFTVERTICALBOTTOM, Stand1State[1][0]);
  move_servo(LEFTVERTICALTOP, Stand1State[1][1]);
  move_servo(LEFTHORIZONTAL, Stand1State[1][2]);
  move_servo(BACKVERTICALBOTTOM, Stand1State[2][0]);
  move_servo(BACKVERTICALTOP, Stand1State[2][1]);
  move_servo(BACKHORIZONTAL, Stand1State[2][2]);
  CurrentState[0][0] = Stand1State[0][0];
  CurrentState[0][1] = Stand1State[0][1];
  CurrentState[0][2] = Stand1State[0][2];
  CurrentState[1][0] = Stand1State[1][0];
  CurrentState[1][1] = Stand1State[1][1];
  CurrentState[1][2] = Stand1State[1][2];
  CurrentState[2][0] = Stand1State[2][0];
  CurrentState[2][1] = Stand1State[2][1];
  CurrentState[2][2] = Stand1State[2][2];
}

void move_servo(int servo_id, int value) {
  pwm.setPWM(servo_id, 0 , value);
}
