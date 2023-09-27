import pyautogui
import time

while True:
    if pyautogui.locateOnScreen('Full Path to image', region=(Full Screen i gess), grayscale=True, confidence=0.5):
        button_loc = pyautogui.locateOnScreen(img, region=(Full Screen i gess), grayscale=True, confidence=0.5)
        pyautogui.click(button_loc)
        print("There you are!")

    print("Where are you?")
    time.sleep(1)
