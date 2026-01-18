#include <Servo.h>

#define ESC_SIGNAL_PIN 10
#define THRUSTER_CALIBRATION_DELAY 5000  // Delay necessary for thruster calibration in milli-seconds.
#define THRUSTER_OPERATION_DELAY 2000    // Non-necessary delay for thruster operation in milli-seconds.
#define STALL_US 1500                    // Duty cycle for stalling thruster in micro-seconds.
#define DUTY_CYCLE_MIN 1350
#define DUTY_CYCLE_MAX 1650

Servo thruster;
int duty_cycle_us = 1350;
int additive = 50;

void setup() {
  // Set thrusters PWM wire to `ESC_SIGNAL_PIN`
  thruster.attach(ESC_SIGNAL_PIN, 1000, 2000);

  // Calibration on startup.
  thruster.writeMicroseconds(STALL_US);
  delay(THRUSTER_CALIBRATION_DELAY);
}

void loop() {
  thruster.writeMicroseconds(duty_cycle_us);
  delay(THRUSTER_OPERATION_DELAY);

  duty_cycle_us += additive;
  if (duty_cycle_us == DUTY_CYCLE_MIN || duty_cycle_us == DUTY_CYCLE_MAX) {
    additive *= -1;
  }
}
