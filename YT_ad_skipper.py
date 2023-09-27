import pyautogui
import time
import cv2

img = cv2.imread("Button.png")

while True:
    if pyautogui.locateOnScreen(img, region=(0,0,1366,768), grayscale=True, confidence=0.5):
        button_loc = pyautogui.locateOnScreen(img, region=(0, 0, 1366, 768), grayscale=True, confidence=0.5)
        pyautogui.click(button_loc)
        print("There you are!")

    print("Where are you?")
    time.sleep(1)