# ulab installation

In this document we study how we can install [ulab](https://github.com/v923z/micropython-ulab), a numpy-like array manipulation library for micropython. Please, first read [the Firmware chapter](https://github.com/v923z/micropython-ulab#firmware) from ulab documentation. At this moment (27.11.2022) there are no ready compilations of ulab to RP2 (Raspberry Pi Pico), but the documentation [contains instructions how compile ulab to RP2-based boards](https://github.com/v923z/micropython-ulab#firmware).

## Compile and build the micropython code

We start by learning how to [compile and build the micropython code](https://docs.micropython.org/en/latest/develop/gettingstarted.html#compile-and-build-the-code).

1. [Get the code](https://docs.micropython.org/en/latest/develop/gettingstarted.html#get-the-code)
  - Follow the given instructions. Notice that you need to open command prompt and change to the directory where you want to clone the repository (for example Documents/github) before you give the clone command (git clone https://github.com/<your-user-name>/micropython)
  - For the development, I created a branch: git checkout -b dev-ulab
2. Compile and build the code
  - We are aiming to compile the code for [RP2 board](https://docs.micropython.org/en/latest/rp2/quickref.html).
    - To Do: Check what are the required dependencies for [RP2 board](https://github.com/micropython/micropython/tree/master/ports/rp2).
3. Building the MicroPython cross-compiler
  - To Do: Got an error: 'make' is not recognized as an internal or external command, operable program or batch file. => Need to install and check needed compilers.
