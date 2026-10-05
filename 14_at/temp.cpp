#include <ros.h>
#include <ros/time.h>
#include <sensor_msgs/Temperature.h>

#define THERMISTOR_PIN       A0
#define SERIES_RESISTOR      10000.0   // 10k fixed resistor
#define THERMISTOR_NOMINAL   10000.0   // 10k thermistor at 25C
#define TEMPERATURE_NOMINAL  25.0      // Nominal temperature (C)
#define B_COEFFICIENT        3950.0    // Beta value (B25/50 or B25/85)
#define ADC_MAX              1023.0
#define NUM_SAMPLES          5

ros::NodeHandle nh;

sensor_msgs::Temperature temp_msg;
ros::Publisher temp_pub("temperature", &temp_msg);

char frame_id[] = "temp_sensor_link";

float readTemperatureC() {
  float adcSum = 0;
  for (int i = 0; i < NUM_SAMPLES; i++) {
    adcSum += analogRead(THERMISTOR_PIN);
    delay(2);
  }
  float adcValue = adcSum / NUM_SAMPLES;

  // Guard against disconnects, floating pins, or rail saturation
  if (adcValue <= 0.5 || adcValue >= (ADC_MAX - 0.5)) {
    return NAN;
  }

  // Voltage divider: 5V -> NTC -> A0 -> Fixed Resistor -> GND
  float resistance = SERIES_RESISTOR / ((ADC_MAX / adcValue) - 1.0);

  // Simplified B-parameter Steinhart-Hart equation
  float steinhart = resistance / THERMISTOR_NOMINAL;        // (R / R0)
  steinhart = log(steinhart);                               // ln(R / R0)
  steinhart /= B_COEFFICIENT;                               // (1 / B) * ln(R / R0)
  steinhart += 1.0 / (TEMPERATURE_NOMINAL + 273.15);         // + (1 / T0)
  steinhart = 1.0 / steinhart;                              // Invert -> Kelvin
  steinhart -= 273.15;                                      // Kelvin -> Celsius

  return steinhart;
}

void setup() {
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.advertise(temp_pub);

  temp_msg.header.frame_id = frame_id;
  temp_msg.variance = 0.05; // Estimated reading variance in deg C^2
}

void loop() {
  float current_temp = readTemperatureC();

  if (!isnan(current_temp)) {
    temp_msg.header.stamp = nh.now();
    temp_msg.temperature = current_temp;
    temp_pub.publish(&temp_msg);
  }

  nh.spinOnce();
  delay(500); // 2 Hz update rate
}