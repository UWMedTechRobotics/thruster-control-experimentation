# Thruster Control Firmware User Manual
### Building the Code
```bash
cd ./stm32_f401re
make all
cd ..
```

### Cleaning the Build Code
```bash
cd ./stm32_f401re
make clean
cd ..
```

### Programming the STM32-F401RE
```bash
cd ./stm32_f401re
STM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
STM32_Programmer_CLI.exe -c port=SWD freq=4000 -w ./build/stm32_f401re.elf 0x08000000
cd ..
```

### Clear the STM32-F401RE
```bash
cd ./stm32_f401re
STM32_Programmer_CLI.exe -c port=SWD freq=4000 -e all
cd ..
```

### Debugging the STM32-F401RE
Consult the [STM32CTL user manual](https://www.st.com/resource/en/user_manual/um3088-stm32cube-commandline-toolset-quick-start-guide-stmicroelectronics.pdf).

### Developing a Driver
To ensure clarity, the driver being created will be referred to as drive.

#### Creating the make scripts:
1. From the project root, open `./thruster-control-firmware/Drivers/custom/src/.` and create a C source file with the given driver's name (e.g. `./drive.c`).

2. From the project root, open `./thruster-control-firmware/Drivers/custom/include/.` and create a C header file with the given driver's name (e.g. `./drive.h`).

3. From the project root, open `./thruster-control-firmware/stm32_f401re/Makefile`.

4. Add the path of the driver's source file to the `# C sources` section.

5. Add the path of the driver's header file to the `# C includes` section.


