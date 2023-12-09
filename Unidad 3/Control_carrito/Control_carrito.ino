#include <SoftwareSerial.h>

SoftwareSerial bt(10,11);
int matrizDireccion[5][4] {
{1, 0, 1, 0},
{0, 1, 0, 1},
{1, 0, 0, 1},
{0, 1, 1, 0},
{0, 0, 0, 0}
};

int matrizVelocidad[5][2] {
{255, 255},
{255, 255},
{255, 127},//,127
{127, 255},//127,
{0, 0}
};

int inputs[]= {2,3,4,5}; //in1, in2, in3, in4 --pines digitales
int enables[]= {6,7}; // pines PWM...
int tc1 = 8; //tcrt5000
int tc2 = 9;
int tc3 = 12;
int tc4 = 13;
int i;
//int estado;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  bt.begin(9600);
  for(i = 0; i<4; i++){
    pinMode(inputs[i], OUTPUT);
  }
  for(i = 0; i<2; i++){
    pinMode(enables[i], OUTPUT);
  }

}

void loop() {
  if(bt.available()>0){
    char status = bt.read();
    int estado = status - '0';
    setDireccion(estado);
  }


}

void setDireccion(int estado){
  for(i = 0; i < 4; i++){
    digitalWrite(inputs[i], matrizDireccion[estado][i]);
  }
  for(i = 0; i < 4; i++){
    analogWrite(enables[i], matrizVelocidad[estado][i]);
  }
}