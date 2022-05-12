#include<ThingSpeak.h>
#include<SoftwareSerial.h>
#include<ESP8266WiFi.h>
SoftwareSerial nodemcu_communication(D1,D2);
WiFiClient client;
float datain1,datain2;
long mychannel = 1722499;
const char apikey[] = "BUAFMVS03GSX8QCJ";
void setup()
{
  Serial.begin(9600);
  nodemcu_communication.begin(9600);
  WiFi.begin("wrc7_fpkhr","p@ssw0rd");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.println("connecting ... ");
    delay(1000);
  }
  Serial.println("NodeMcu connected");
  Serial.println(WiFi.localIP());
  ThingSpeak.begin(client);
  delay(500);
}
void loop()
{
 while (nodemcu_communication.available()>0)
 {
  datain1 = nodemcu_communication.read();
  datain2 = nodemcu_communication.read();
  Serial.println(datain1);
  Serial.println(datain2);
  ThingSpeak.setField(1,datain1);
  ThingSpeak.setField(2,datain2);
   ThingSpeak.writeFields(mychannel,apikey);
//  ThingSpeak.writeField(mychannel,2,datain2,apikey);
  delay(5000);
 }
}
