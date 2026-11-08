#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle nh;
std_msgs::Int32 msg;
ros::Publisher pub("gas_sensor", &msg);

void setup() {
  nh.initNode();
  nh.advertise(pub);
}

void loop() {
  msg.data = 1023 - analogRead(A0);
  pub.publish(&msg);
  nh.spinOnce();
  delay(100);
}