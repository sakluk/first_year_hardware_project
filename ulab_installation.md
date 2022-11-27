# ulab installation

[ulab](https://github.com/v923z/micropython-ulab) is a numpy-like array manipulation library for micropython. It is not included in the standard micropython firmware installed with [Thonny's Interpreter](https://github.com/thonny/thonny/wiki/MicroPython#firmware-installation--upgrade). In order to have ulab working for your RP2 board, you need to install a [special firmware](https://github.com/v923z/micropython-builder/releases) manually on your RP2 boards. Here are quick instructions.

1. Push and hold the BOOTSEL button and plug your Pico into the USB board. It will mount as a mass storage device called RPI-RP2 to your computer.
2. Copy the PICO.uf2 file from the [ulab micropython releases](https://github.com/v923z/micropython-builder/releases).
3. Drag and drop the micropython UF2 file into onto the RPI-RP2 volume. Your pico will reboot. You are now running micropython with ulab in your pico.
4. Open Thonny.
5. Write a simple test demo:

  from ulab import numpy as np
  x = np.ones(5)
  print(x)

If this code works, you have a working micropython firmware with ulab.

To do (27.11.2022):
- Check if Pico Wireless works with micropython with ulab firmware.

More info:
- [ulab micropython builder](https://github.com/v923z/micropython-builder)
- [Drag and drop micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython)
- [ulab - firmware](https://github.com/v923z/micropython-ulab#firmware)
- [Thonny - micropython firmware installation upgrade](https://github.com/thonny/thonny/wiki/MicroPython#firmware-installation--upgrade)
- [ulab - how to compile ulab to RP2-based boards](https://github.com/v923z/micropython-ulab#firmware).


