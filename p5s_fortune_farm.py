import pyautogui
import pydirectinput

pyautogui.hotkey('alt', 'tab')

pyautogui.sleep(1)
pydirectinput.moveTo(960,540)
pydirectinput.leftClick

pydirectinput.FAILSAFE = False
while (True):
    pydirectinput.keyDown('w')
    pyautogui.sleep(2)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('j')
    pyautogui.sleep(0.9)
    pydirectinput.keyUp('j')
    pydirectinput.keyDown('w')
    pyautogui.sleep(2.8)
    pydirectinput.keyUp('w')

    pydirectinput.press('n')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(1)
    pydirectinput.press('space')
    pyautogui.sleep(2)
    pydirectinput.press('space')
    pyautogui.sleep(2)
    pydirectinput.press('1')
    pyautogui.sleep(0.5)
    pydirectinput.press('down')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(1)

    pydirectinput.press('1')
    pyautogui.sleep(0.5)
    pydirectinput.press('down')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(3)

    pydirectinput.press('1')
    pyautogui.sleep(0.5)
    pydirectinput.press('up')
    pyautogui.sleep(0.5)
    pydirectinput.press('space')
    pyautogui.sleep(3)