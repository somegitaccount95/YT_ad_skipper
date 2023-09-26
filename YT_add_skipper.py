import pyautogui
import time
import keyboard
import win32api, win32con

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('(insrt key)') == False:
    if pyautogui.locateOnScreen('button.png', region=(0,0,1366,768), grayscale=True, confidence=0.5) != None:
        click()
