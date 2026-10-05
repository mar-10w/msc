#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Range.h>

ros::NodeHandle nh;

sensor_msgs::Range range_msg;
ros::Publisher range_pub("ultrasonic/range", &range_msg);

const int TRIG_PIN = 9;
const int ECHO_PIN = 10;

// Maximum expected range timeout (~3.0 meters: 300cm * 2 / 0.0343 ≈ 17500 us)
const unsigned long TIMEOUT_US = 18000; 

char frame_id[] = "ultrasonic_link";

void setup()
{
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.advertise(range_pub);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Configure static Range fields
  range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
  range_msg.header.frame_id = frame_id;
  range_msg.field_of_view = 0.26; // ~15 degrees in radians
  range_msg.min_range = 0.02;     // 2 cm
  range_msg.max_range = 3.00;     // 3 m
}

void loop()
{
  // Trigger 10us pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Measure round-trip time with timeout
  long duration = pulseIn(ECHO_PIN, HIGH, TIMEOUT_US);

  range_msg.header.stamp = nh.now();

  if (duration > 0)
  {
    // Convert to meters: (duration * 0.0343 cm/us) / 2.0 / 100.0
    float distance_m = (duration * 0.000343) / 2.0;
    range_msg.range = distance_m;
  }
  else
  {
    // If no echo, set to infinity or max_range per ROS convention
    range_msg.range = range_msg.max_range;
  }

  range_pub.publish(&range_msg);

  nh.spinOnce();
  delay(60); // Publish at ~15 Hz
}