
#include <SoftwareSerial.h> 
SoftwareSerial MyBlue(0, 1); // RX | TX 
int flag = 0; 
int LED = 13; 
void setup() 
{   
 Serial.begin(9600); 
 MyBlue.begin(9600); 
 pinMode(LED, OUTPUT); 
 pinMode(0,INPUT);
 pinMode(1, OUTPUT);
 Serial.println("Ready to connect\nDefualt password is 1234 or 000"); 
} 
void loop() 
{ 
  Serial.println(MyBlue.available());
 if (MyBlue.available()) 
   flag = MyBlue.read(); 
 if (flag == 1) 
 { 
   digitalWrite(LED, HIGH); 
   Serial.println("LED On"); 
 } 
 else if (flag == 0) 
 { 
   digitalWrite(LED, LOW); 
   //Serial.println("LED Off"); 
 } 
}  
