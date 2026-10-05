#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle nh;

std_msgs::Int32 flex_msg;
ros::Publisher flex_pub("flex_sensor", &flex_msg);

const int FLEX_PIN = A1;

void setup()
{
  nh.getHardware()->setBaud(57600); // Standard rosserial baud rate
  nh.initNode();
  nh.advertise(flex_pub);

  // Analog pins on AVR/Arduino are input by default, but explicit declaration is fine
  pinMode(FLEX_PIN, INPUT);
}

void loop()
{
  flex_msg.data = analogRead(FLEX_PIN);
  flex_pub.publish(&flex_msg);

  nh.spinOnce();
  delay(100); // ~10 Hz publish rate
}