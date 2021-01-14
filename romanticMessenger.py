import pyautogui
import time
message = 10
while message > 0:
    time.sleep(2)
    pyautogui.typewrite("Yeee I done this")
    time.sleep(1)
    pyautogui.press('enter')
    message = message - 1


