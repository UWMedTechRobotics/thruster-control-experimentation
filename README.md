# Thruster Controls Experimentation Firmware

## Requirements
1. [ ] Communicates with user via serial port.
2. [ ] Interface with ESC to control the thruster's speed.
3. [ ] Log frequency into spreadsheet upon request from user.

## Specifications
For Requirement 1:
- [ ] Write Python script using Serial.py for sending serial data to the STM32.
- [ ] Write driver for the STM32 for interfacing with the computer's Python script.
  - Either make this interrupt driven, or ran on a separate thread.
- [ ] Create GUI in Python using PySimpleGUI for sending and receiving data.
  - Upon data received, GUI should allow for user to input scale reading.

For Requirement 2:
- [ ] Write driver for the STM32 for interfacing with the ESC via PWM.
  - Speed control input should be based off of duty cycle %.

For Requirement 3:
- [ ] Write script in Python for writing received data into a JSON file.
- [ ] Research how to export the JSON file into Excel.