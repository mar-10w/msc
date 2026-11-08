#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle nh;
std_msgs::Float32 msg;
ros::Publisher pub("range", &msg);

void setup() {
  nh.initNode();
  nh.advertise(pub);
  pinMode(9, OUTPUT);
}

void loop() {
  digitalWrite(9, HIGH);
  delayMicroseconds(10);
  digitalWrite(9, LOW);

  msg.data = pulseIn(10, HIGH, 18000) / 58.0;
  pub.publish(&msg);
  nh.spinOnce();
  delay(100);
}