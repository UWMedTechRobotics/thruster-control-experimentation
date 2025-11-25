import serial   # type: ignore
import re
import json
import struct


COMMAND_SUCCESS = 0
COMMAND_WARNING_COMMAND_MISMATCH = 1
COMMAND_ERROR_INVALID = -1
COMMAND_ERROR_UNKNOWN = -2


def main():
  com_port_match = None
  while com_port_match == None:
    com_port = input("COM Port: ")
    com_port_match = re.match(r"COM(\d+)", com_port)

  with serial.Serial() as ser:
    ser.baudrate = 19200
    ser.port = com_port
    ser.open()

    status = -1
    while True:
      command = input("Type Command: ")

      status = set_duty_cycle_percentage(command, ser)
      if status != COMMAND_WARNING_COMMAND_MISMATCH:
        continue
      
      status = log_data(command, ser)
      if status != COMMAND_WARNING_COMMAND_MISMATCH:
        continue

      status = close_serial(command, ser)
      if status == COMMAND_SUCCESS:
        break


def set_duty_cycle_percentage(command: str, ser: serial.Serial) -> int:
  command_match = re.match(r"set-dcp (\w+)", command)

  if command_match != None:
    try:
      dcp = float(command_match.group(1))
      ser.write(f"set-dcp {dcp}")
      return COMMAND_SUCCESS
    
    except ValueError:
      print("Invalid duty cycle percent!")
      return COMMAND_ERROR_INVALID
  
  return COMMAND_WARNING_COMMAND_MISMATCH
  

def log_data(command: str, ser: serial.Serial) -> int:
  number_regex = re.compile(r"""log ^[+-]?(\d+(\.\d*)? | \.\d+)$""", re.VERBOSE)
  command_match = number_regex.match(command)
  
  if command_match == None:
    return COMMAND_WARNING_COMMAND_MISMATCH
  
  try:
    thrust_in_kilograms = float(command_match.group(1))
    ser.write("get-dcp")
    response = ser.read_until(b"\n")
    duty_cycle_percentage = struct.unpack('f', response)[0]

    if write_json_entry_to_json_array(duty_cycle_percentage, thrust_in_kilograms) != COMMAND_SUCCESS:
      return COMMAND_ERROR_UNKNOWN

  except ValueError:
    print("Invalid thrust in kilograms")
    return COMMAND_ERROR_INVALID
  

def close_serial(command: str, ser: serial.Serial) -> int:
  if command != "close":
    return COMMAND_WARNING_COMMAND_MISMATCH
  
  print(f"Closing {ser.port}")

  return COMMAND_SUCCESS


def write_json_entry_to_json_array(duty_cycle_percentage: float, thrust_in_kilograms: float):
  with open("./data_log.json", "r+") as data_log:
    loaded_python_list = []
    try:
      loaded_python_list = json.load(data_log)
      json_entry = {
        "Duty Cycle %" : duty_cycle_percentage,
        "Thrust in KG" : thrust_in_kilograms
      }
      loaded_python_list.append(json_entry)

    except json.JSONDecodeError:
      return COMMAND_ERROR_UNKNOWN
    
    except UnicodeDecodeError:
      return COMMAND_ERROR_UNKNOWN

    json.dump(loaded_python_list, data_log)
  
  return COMMAND_SUCCESS


  

if __name__ == "__main__":
  main()