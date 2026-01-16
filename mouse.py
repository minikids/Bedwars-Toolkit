from pynput.mouse import Button, Controller
import time

mouse = Controller()

def click():
    mouse.press(Button.left)
    mouse.release(Button.left)
