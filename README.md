# MacrOUT MK1

Raspberry Pi Pico based, macro keyboard for F13-F24.

## Configuration 

Buttons must be connected to 3V3OUT pin and any digital pins. In default, I connected where the pins down below, I chose them for make my PCB more tidy.

**Default Pins:** _GP0, GP1, GP3, GP4, GP6, GP7, GP9, GP10, GP13, GP14, GP15, GP16_

![My PCB design, for 100x50mm one layer copper plate](https://user-images.githubusercontent.com/70312743/222145856-87ac37a0-db8d-4cfd-b09b-9b4d7018bba1.png)

## Setup 

### Requirements

*   [Adafruit CircuitPython Driver](https://circuitpython.org/board/raspberry_pi_pico/)

After you setup driver, you need to change the "code.py" where in Pico with in GitHub one. You can change the pins from code.py as you wish.
