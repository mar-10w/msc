#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle nh;

std_msgs::Int32 gas_msg;
ros::Publisher gas_pub("gas_sensor", &gas_msg);

const int GAS_PIN = A0;
const int SAMPLES = 8; // Multi-sampling to filter ADC ripple

void setup()
{
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.advertise(gas_pub);

  pinMode(GAS_PIN, INPUT);
}

void loop()
{
  // Average multiple readings to eliminate heater switching/ADC noise
  long sum = 0;
  for (int i = 0; i < SAMPLES; i++) {
    sum += analogRead(GAS_PIN);
    delayMicroseconds(50);
  }
  
  gas_msg.data = sum / SAMPLES;
  gas_pub.publish(&gas_msg);

  nh.spinOnce();
  delay(100); // 10 Hz publish rate
}