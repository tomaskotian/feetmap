//----------------------------------------------------------
//feetmap_v0_sensors

//program which read data from 10 HX711 a send them via USB after 'S' send from computer via Serial
//HX711 rate 10SPS, pin 15 GND

//Connection sensor to HX711
//RED   E+
//BLACK E-
//GREEN A-
//WHITE A+

//Sensor
//white cable down and sensor on static body

//Segment anotiation when you stand on feetmap
//message L1-<value>
//start with L1,L2,.....R1,...,R5
//left foot     right foot
//L1  L2        R1  R2
//  L3            R3
//L4  L5        R4  R5

//usb 
//baud rate 115200

//read all sensors with common SCLK for one foot

//Conector male front side
// 1 2 3 4 5
//  9 8 7 6
//1 red VCC
//2 black GND
//3 blue DT_L1
//4 purple DT_L2
//5 shield GND
//6 yellow DT_L3
//7 green DT_L4
//8 brown DT_L5 
//9 white SCLK_L
//----------------------------------------------------------

#define R_FOOT 0
#define L_FOOT 1


//left foot
#define DT_L1 A0
#define DT_L2 A1
#define DT_L3 A2
#define DT_L4 A3
#define DT_L5 A4
#define SCLK_L A5
//right foot
#define DT_R1 2
#define DT_R2 3
#define DT_R3 4
#define DT_R4 5
#define DT_R5 6
#define SCLK_R 7

uint32_t l_foot[5];
uint32_t r_foot[5];



void setup() {


  l_foot[0] = 32600000;
  l_foot[1] = 31600000;
  l_foot[2] = 30600000;
  l_foot[3] = 29600000;
  r_foot[0] = 32600000;
  r_foot[1] = 31600000;
  r_foot[2] = 30600000;
  r_foot[3] = 29600000;
  Serial.begin(115200);
  //left foot
  pinMode(DT_L1, INPUT);
  pinMode(DT_L2, INPUT);
  pinMode(DT_L3, INPUT);
  pinMode(DT_L4, INPUT);
  pinMode(DT_L5, INPUT);
  pinMode(SCLK_L, OUTPUT);
  digitalWrite(SCLK_L, LOW);
  //right foot
  pinMode(DT_R1, INPUT);
  pinMode(DT_R2, INPUT);
  pinMode(DT_R3, INPUT);
  pinMode(DT_R4, INPUT);
  pinMode(DT_R5, INPUT);
  pinMode(SCLK_R, OUTPUT);
  digitalWrite(SCLK_R, LOW);
}

void ReadSensors(){
      for(int i=0; i < 5; i++){
        Serial.print("L");
        Serial.print(i+1);
        Serial.print("-");
        Serial.println(l_foot[i]);
      }
      for(int i=0; i < 5; i++){
        Serial.print("R");
        Serial.print(i+1);
        Serial.print("-");
        Serial.println(r_foot[i]);
      }
}

void loop() {
  if(Serial.available() > 0){
    if ('S' == Serial.read()){
      ReadSensors();
    }
  }
}


    

    
  
  