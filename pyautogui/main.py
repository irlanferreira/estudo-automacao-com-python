import time

import pyautogui

time.sleep(1)
pyautogui.click()
pyautogui.keyDown('shift')
pyautogui.typewrite('aaaa')
pyautogui.keyUp('shift')