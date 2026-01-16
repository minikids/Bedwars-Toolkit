import mouse
from pynput import keyboard
import time
import threading
from ctypes import *

cdll.LoadLibrary("main.dylib")

dylib = CDLL("main.dylib")

delay : int = int()

readFile = dylib.readFile

readFile.restype = c_char_p

if (dylib.isFile(b"delay.settings") == 1):
    delay = float(readFile(b"delay.settings"))
else:
    inputcontent = input("Enter delay between clicks (in seconds): ").encode()
    delay = float(inputcontent)
    dylib.writeFile(b"delay.settings", inputcontent)

start_click = dylib.start_click

def onClick(key):
    global start_click
    try:
        if key.char == '[':
            start_click = 1
    except:
        pass

def onRelease(key):
    global start_click
    try:
        if key.char == '[':
            start_click = 0
    except:
        pass

quit_main = False

def main():
    global start_click
    global delay
    while quit_main == False:
        if start_click == 1:
            mouse.click()
            time.sleep(delay)

mainthread = threading.Thread(target=main)

mainthread.start()
try:
    with keyboard.Listener(on_press=onClick, on_release=onRelease) as l:
        l.join()
except KeyboardInterrupt:
    quit_main = True
