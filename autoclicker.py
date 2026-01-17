from pynput import keyboard
import pyautogui
import time
import threading
from ctypes import *
import dylib

cps = int()

readFile = dylib.readFile

readFile.restype = c_char_p

if (dylib.isFile(b"cps.settings") == 1):
    cps = float(readFile(b"cps.settings"))
else:
    inputcontent = input("Enter CPS: ").encode()
    cps = float(inputcontent)
    dylib.writeFile(b"cps.settings", inputcontent)

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
    global cps
    while quit_main == False:
        if start_click == 1:
            pyautogui.click(_pause = False, clicks=round(cps / 33), interval=1/(cps))
        time.sleep(0.05)

mainthread = threading.Thread(target=main)

mainthread.start()
try:
    with keyboard.Listener(on_press=onClick, on_release=onRelease) as l:
        l.join()
except KeyboardInterrupt:
    quit_main = True
    mainthread.join()
