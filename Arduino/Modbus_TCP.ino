/**
  Autor: David De Armas
  Fecha: 26/02/2024
  
  Control de un servo mediante Modbus TCP
  Se utiliza un Arduino UNO y una Ethernet shield V1.0
  
  Basado en el ejemplo de:
  
  @file Servo.ino
  Modbus-Arduino Example - Servo (Modbus TCP using Ethernet shield)
  Copyright by André Sarmento Barbosa
  https://github.com/epsilonrt/modbus-ethernet
*/

#include <Modbus.h>
#include <ModbusEthernet.h>
#include <Servo.h>

// Modbus Registers Offsets (0-9999)
const int SERVO_HREG = 0; 
// Used Pins
const int servoPin = 9;

// ModbusEthernet object
ModbusEthernet mb;
// Servo object
Servo servo; 

void setup() {
    //Serial.begin(9600);
    // The media access control (ethernet hardware) address for the shield
    // Change the MAC address as you like for Ethernet shield V1.0
    byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };  
    // The IP address for the shield
    byte ip[] = { 192, 168, 0,  200};   
    // Config Modbus TCP 
    mb.config(mac, ip);
    // Attaches the servo pin to the servo object
    servo.attach(servoPin); 
    // Add SERVO_HREG register - Use addHreg() for analog outpus or to store values in device 
    mb.addHreg(SERVO_HREG, 90);
}

void loop() {
   //Call once inside loop() - all magic here
   mb.task();
   servo.write(mb.Hreg(SERVO_HREG));
   //Serial.println(mb.Hreg(SERVO_HREG));
   delay(30);
}
