# Thruster Controls Experimentation Firmware
For details regarding testing results, refer to the [Test Results Table](https://uofwaterloo-my.sharepoint.com/:x:/g/personal/aetarant_uwaterloo_ca/IQDWStpDtX5dRLZYZ64iAWjNAaUsucCty3hMAVqpXVbz9dc?e=oviBQm).

## Setup Instructions
1. Connect Arduino Uno's pin 10* to the PWM signal wire (orange wire) of a given ESC, 
connect ground wire of ESC (brown wire) to ground of the Arduino Uno.
2. Connect the ESC to a power source**
3. Connect the ESC to the thruster

(*) Pin used can be changed by editing `ESC_SIGNAL_PIN` in `src/main.ino`. Note that
the pin used must be PWM compatible. Typically Arduino Uno's denote PWM compatible 
pins with a ~.

(**) The given power source must be able to supply a minimum of 3A at 24V DC.