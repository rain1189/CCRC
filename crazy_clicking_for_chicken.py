import sys
import time
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

준비시간 = float(sys.argv[1])
쉬는시간 = float(sys.argv[2])
횟수 = int(sys.argv[3])

time.sleep(준비시간)
for i in range(횟수):
    mouse.click(Button.left)
    time.sleep(쉬는시간)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(쉬는시간)