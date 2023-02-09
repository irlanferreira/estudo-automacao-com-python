import time

import pyautogui
while True:
    pos = pyautogui.position()
    scr = pyautogui.screenshot()
    cor = scr.getpixel(pyautogui.position())
    txt = f'A posição atual é {pos}, a cor é {cor}.'
    print(txt, end='')
    time.sleep(2)
    caracs = len(txt)
    for c in range(caracs):
        print('\b', end='')
