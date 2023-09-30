import pyautogui
import time
from pyautogui import locateOnScreen

print("Press Ctrl + C to quit")

while True:
    mouse_pos = pyautogui.position()
    if pyautogui.locateOnScreen('Button.png', grayscale=True, confidence=0.5):
        button_loc = pyautogui.locateOnScreen('Button.png', grayscale=True, confidence=0.5)
        pyautogui.click(button_loc)
        pyautogui.moveTo(mouse_pos)

    time.sleep(1)
