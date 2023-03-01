import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP3
btn4_pin = board.GP4
btn5_pin = board.GP6
btn6_pin = board.GP7
btn7_pin = board.GP9
btn8_pin = board.GP10
btn9_pin = board.GP13
btn10_pin = board.GP14
btn11_pin = board.GP15
btn12_pin = board.GP16

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

page = 1

while True:
    if btn1.value:
        keyboard.press(0x68)
    if btn1.value == 0:
        keyboard.release(0x68)

    if btn2.value:
        keyboard.press(0x69)
    if btn2.value == 0:
        keyboard.release(0x69)

    if btn3.value:
        keyboard.press(0x6A)
    if btn3.value == 0:
        keyboard.release(0x6A)

    if btn4.value:
        keyboard.press(0x6B)
    if btn4.value == 0:
        keyboard.release(0x6B)

    if btn5.value:
        keyboard.press(0x6C)
    if btn5.value == 0:
        keyboard.release(0x6C)

    if btn6.value:
        keyboard.press(0x6D)
    if btn6.value == 0:
        keyboard.release(0x6D)

    if btn7.value:
        keyboard.press(0x6E)
    if btn7.value == 0:
        keyboard.release(0x6E)

    if btn8.value:
        keyboard.press(0x6F)
    if btn8.value == 0:
        keyboard.release(0x6F)

    if btn9.value:
        keyboard.press(0x70)
    if btn9.value == 0:
        keyboard.release(0x70)

    if btn10.value:
        keyboard.press(0x71)
    if btn10.value == 0:
        keyboard.release(0x71)

    if btn11.value:
        keyboard.press(0x72)
    if btn11.value == 0:
        keyboard.release(0x72)

    if btn12.value:
        keyboard.press(0x73)
    if btn12.value == 0:
        keyboard.release(0x73)
