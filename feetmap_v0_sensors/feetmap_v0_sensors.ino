//----------------------------------------------------------
//feetmap_v0_sensors

//program which read data from 10 HX711 a send them via USB after 'S' send from computer via Serial
//HX711 rate 10SPS, pin 15 GND

//Connection sensor to HX711
//RED   E+
//BLACK E-
//GREEN A-
//WHITE A+

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

void loop() {
  if(Serial.available() > 0){
    if ('S' == Serial.read()){
      ReadSensors();
    }
  }
}

void ReadSensors(){
  //if(!(digitalRead(DT_L1) && digitalRead(DT_L2) && digitalRead(DT_L3) && digitalRead(DT_L4) && digitalRead(DT_L5))) //for all sensors
    if(!(digitalRead(DT_L1))) //for testing one sensor
    {
      digitalWrite(SCLK_L, LOW);
      l_foot[0] = 0;
      l_foot[1] = 0;
      l_foot[2] = 0;
      l_foot[3] = 0;
      l_foot[4] = 0;
      bool tmp[5];
      for(int i = 24; i >= 0; i--)
      {
        digitalWrite(SCLK_L, HIGH);
        delayMicroseconds(1);
        tmp[0] = digitalRead(DT_L1);
        tmp[1] = digitalRead(DT_L2);
        tmp[2] = digitalRead(DT_L3);
        tmp[3] = digitalRead(DT_L4);
        tmp[4] = digitalRead(DT_L5);
        digitalWrite(SCLK_L, LOW);
        delayMicroseconds(1);
        l_foot[0] |= ((uint32_t)(tmp[0]) << i);
        l_foot[1] |= ((uint32_t)(tmp[1]) << i);
        l_foot[2] |= ((uint32_t)(tmp[2]) << i);
        l_foot[3] |= ((uint32_t)(tmp[3]) << i);
        l_foot[4] |= ((uint32_t)(tmp[4]) << i);
      }
      for(int i=0; i < 5; i++){
        Serial.print("L");
        Serial.print(i+1);
        Serial.print("-");
        Serial.println(l_foot[i]);
      }
    }

    //if(!(digitalRead(DT_R1) && digitalRead(DT_R2) && digitalRead(DT_R3) && digitalRead(DT_R4) && digitalRead(DT_R5)))
    // {
    //   digitalWrite(SCLK_R, LOW);
    //   r_foot[0] = 0;
    //   r_foot[1] = 0;
    //   r_foot[2] = 0;
    //   r_foot[3] = 0;
    //   r_foot[4] = 0;
    //   bool tmp[5];
    //   for(int i = 24; i >= 0; i--)
    //   {
    //     digitalWrite(SCLK_R, HIGH);
    //     delayMicroseconds(1);
    //     tmp[0] = digitalRead(DT_R1);
    //     tmp[1] = digitalRead(DT_R2);
    //     tmp[2] = digitalRead(DT_R3);
    //     tmp[3] = digitalRead(DT_R4);
    //     tmp[4] = digitalRead(DT_R5);
    //     digitalWrite(SCLK_R, LOW);
    //     delayMicroseconds(1);
    //     r_foot[0] |= ((uint32_t)(tmp[0]) << i);
    //     r_foot[1] |= ((uint32_t)(tmp[1]) << i);
    //     r_foot[2] |= ((uint32_t)(tmp[2]) << i);
    //     r_foot[3] |= ((uint32_t)(tmp[3]) << i);
    //     r_foot[4] |= ((uint32_t)(tmp[4]) << i);
    //   }
    //   for(int i=0; i < 5; i++){
    //     Serial.print("R");
    //     Serial.print(i+1);
    //     Serial.print("-");
    //     Serial.println(r_foot[i]);
    //   }
    // }
}
    

    
  
  