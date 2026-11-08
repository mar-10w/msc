#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle nh;
std_msgs::Float32 msg;
ros::Publisher pub("temperature", &msg);

void setup() {
  nh.initNode();
  nh.advertise(pub);
}

void loop() {
  float r = 10000.0 / (1023.0 / analogRead(A0) - 1.0);
  msg.data = (1.0 / (0.003354 + 0.000253 * log(r / 10000.0))) - 273.15;

  pub.publish(&msg);
  nh.spinOnce();
  delay(500);
}